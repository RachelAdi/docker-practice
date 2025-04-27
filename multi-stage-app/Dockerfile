# Stage 1: Build dependencies
FROM python:3.9-slim AS builder

WORKDIR /app

# עדכון חבילות והתקנת כלי בנייה
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    gfortran \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# יצירת קבצי wheel
RUN pip wheel --no-cache-dir --wheel-dir /app/wheels -r requirements.txt

# Stage 2: Final image
FROM python:3.9-slim

WORKDIR /app

# התקנת pip והעתקת קבצי wheel
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*

COPY app.py .

CMD ["python", "app.py"]

