FROM python:3.12-slim

WORKDIR /app
COPY . /app

CMD ["python", "run_sim.py", "--loop", "--interval", "600"]
