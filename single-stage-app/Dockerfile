FROM python:3.9

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create output directory
RUN mkdir -p output

# Run the application
CMD ["python", "app.py"]
