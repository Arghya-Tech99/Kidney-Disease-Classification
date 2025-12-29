
FROM python:3.8-slim-bullseye

# Adding a 'fix' for the repository sync issue
RUN apt-get update --fix-missing -y && \
    apt-get install -y --no-install-recommends awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "app.py"]