# Step 1: Use the official Python 3.13 slim image
FROM python:3.13-slim-bookworm

# Step 2: Install system dependencies
# Added libbz2-dev and liblzma-dev which are often needed for 3.13 wheels
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    awscli \
    gcc \
    python3-dev \
    libexpat1 \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Step 3: Copy project files
COPY . /app

# Step 4: Install Python dependencies
# We use --pre to allow 'pre-release' versions because stable
# TensorFlow versions for 3.13 might not exist yet.
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Step 5: Start the application
CMD ["python3", "app.py"]