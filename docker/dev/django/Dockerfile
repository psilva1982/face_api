# Pull base image
FROM python:3.11-slim

# python
# Set environment variables
ENV PYTHONUNBUFFERED 1
# prevents python creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# pip
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

## Install environment dependencies
RUN apt-get update && apt-get -y install git wget libgl1-mesa-glx libglib2.0-0 libsm6 libxrender1 libxext6 python3-dev build-essential cmake gettext python3-setuptools libmagic-dev libpq-dev \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# create folder
RUN mkdir -p /face_api


# Set work directory
WORKDIR /face_api

# Copy project
COPY . /face_api/

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config installer.max-workers 10
RUN poetry config virtualenvs.create false
RUN poetry install --ansi -vvv
