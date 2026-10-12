"""
HTTP/TLS Client with RFC-compliant TLS ClientHello Record Fragmentation.
Allows direct, zero-VPN access to Polymarket Gamma API & CLOB API even under DPI SNI inspection,
while preserving full SSL certificate verification (TLS 1.3).
"""

import gzip
import json
import socket
import ssl
import time
import urllib.parse
import urllib.request
import zlib
from typing import Any, Dict, Optional


def fetch_polymarket_json(
    host: str,
    path: str,
    timeout: float = 12.0,
    retries: int = 2,
) -> Any:
    """
    Fetches JSON from a Polymarket host (gamma-api.polymarket.com or clob.polymarket.com)
    using TLS ClientHello record fragmentation to bypass passive DPI SNI filtering.
    """
    last_err: Optional[Exception] = None
    for attempt in range(retries + 1):
        sock: Optional[socket.socket] = None
        try:
            in_bio = ssl.MemoryBIO()
            out_bio = ssl.MemoryBIO()
            ctx = ssl.create_default_context()
            ssl_obj = ctx.wrap_bio(in_bio, out_bio, server_hostname=host)

            sock = socket.create_connection((host, 443), timeout=timeout)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

            try:
                ssl_obj.do_handshake()
            except ssl.SSLWantReadError:
                pass

            hello = out_bio.read()
            if len(hello) > 10 and hello[0] == 0x16:
                rec_hdr = hello[:3]
                payload = hello[5:]
                # Split ClientHello payload into 3 small TLS records so SNI is split across records
                p1 = payload[:24]
                p2 = payload[24:96]
                p3 = payload[96:]
                frag1 = rec_hdr + len(p1).to_bytes(2, "big") + p1
                frag2 = rec_hdr + len(p2).to_bytes(2, "big") + p2
                frag3 = rec_hdr + len(p3).to_bytes(2, "big") + p3
                sock.sendall(frag1)
                sock.sendall(frag2)
                sock.sendall(frag3)
            else:
                sock.sendall(hello)

            while True:
                try:
                    ssl_obj.do_handshake()
                    break
                except ssl.SSLWantReadError:
                    out_d = out_bio.read()
                    if out_d:
                        sock.sendall(out_d)
                    in_d = sock.recv(32768)
                    if not in_d:
                        raise EOFError(f"Connection closed during TLS handshake with {host}")
                    in_bio.write(in_d)

            out_d = out_bio.read()
            if out_d:
                sock.sendall(out_d)

            req_str = (
                f"GET {path} HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\r\n"
                f"Accept: application/json\r\n"
                f"Accept-Encoding: gzip, deflate\r\n"
                f"Connection: close\r\n\r\n"
            )
            ssl_obj.write(req_str.encode("utf-8"))
            sock.sendall(out_bio.read())

            raw_resp = bytearray()
            while True:
                try:
                    chunk = ssl_obj.read(32768)
                    if not chunk:
                        break
                    raw_resp.extend(chunk)
                except ssl.SSLWantReadError:
                    in_d = sock.recv(32768)
                    if not in_d:
                        break
                    in_bio.write(in_d)
                except ssl.SSLZeroReturnError:
                    break

            sock.close()
            sock = None

            if b"\r\n\r\n" not in raw_resp:
                raise ValueError(f"Invalid HTTP response from {host}{path}")

            hdr_bytes, body_bytes = bytes(raw_resp).split(b"\r\n\r\n", 1)
            hdr_text = hdr_bytes.decode("iso-8859-1", errors="replace")
            status_line = hdr_text.splitlines()[0] if hdr_text else ""
            if " 200 " not in status_line:
                raise RuntimeError(f"HTTP error from {host}{path}: {status_line}")

            hdr_lower = hdr_text.lower()

            # Decode chunked transfer encoding if present
            if "transfer-encoding: chunked" in hdr_lower:
                decoded = bytearray()
                buf = body_bytes
                while buf:
                    idx = buf.find(b"\r\n")
                    if idx == -1:
                        break
                    line = buf[:idx]
                    buf = buf[idx + 2 :]
                    size_str = line.split(b";")[0].strip()
                    if not size_str:
                        continue
                    chunk_size = int(size_str, 16)
                    if chunk_size == 0:
                        break
                    decoded.extend(buf[:chunk_size])
                    buf = buf[chunk_size + 2 :]
                body_bytes = bytes(decoded)

            # Decompress gzip / deflate if present
            if "content-encoding: gzip" in hdr_lower:
                body_bytes = gzip.decompress(body_bytes)
            elif "content-encoding: deflate" in hdr_lower:
                body_bytes = zlib.decompress(body_bytes)

            return json.loads(body_bytes.decode("utf-8"))

        except Exception as e:
            last_err = e
            if sock is not None:
                try:
                    sock.close()
                except Exception:
                    pass
            if attempt < retries:
                time.sleep(0.5 * (attempt + 1))

    raise RuntimeError(f"Failed to fetch https://{host}{path} after {retries + 1} attempts: {last_err}")


def fetch_standard_url(
    url: str,
    timeout: float = 10.0,
    as_json: bool = True,
    headers: Optional[Dict[str, str]] = None,
) -> Any:
    """Standard HTTPS fetch for non-blocked APIs (Binance, Open-Meteo, Google News RSS, etc.)."""
    req_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PolymarketPaperSim/1.0",
        "Accept": "application/json, application/xml, text/xml, */*",
    }
    if headers:
        req_headers.update(headers)

    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
        text = data.decode("utf-8", errors="replace")
        if as_json:
            return json.loads(text)
        return text
