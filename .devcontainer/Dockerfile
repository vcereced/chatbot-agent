FROM mcr.microsoft.com/devcontainers/python:3.12

# Herramientas útiles
RUN apt-get update && apt-get install -y \
    git \
    make \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Herramientas de Python
RUN pip install --upgrade pip