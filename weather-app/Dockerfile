FROM python:3.9-alpine

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the application code
COPY weather.py .

CMD ["python", "weather.py"]
