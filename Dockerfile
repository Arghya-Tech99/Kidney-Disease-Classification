FROM python:3.8-slim-bullseye

# Install awscli AND build tools needed for heavy python packages
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Use --no-cache-dir to save space and prevent memory crashes in GitHub Actions
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]