FROM python:3.8-slim-buster

# We use apt-get for stability in scripts and DEBIAN_FRONTEND to skip prompts
# The rm -rf line keeps the image small by deleting the cache after installation
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Best practice: upgrade pip first to avoid installation issues with newer packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "app.py"]