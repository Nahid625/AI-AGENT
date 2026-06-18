FROM python:3.12-slim

WORKDIR /src

# Install system dependencies if needed
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Railway provides PORT automatically
ENV PORT=8000

# Change line 19 from the old array format to this exact line:
CMD uvicorn main:app --host 0.0.0.0 --port $PORT