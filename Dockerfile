# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy Python requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install redis-py-cluster

# Copy the rest of the application
COPY . /app/

# Run the application
CMD ["python", "main.py"]
