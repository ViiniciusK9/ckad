FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

ENV API_URL=http://localhost:8000

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
