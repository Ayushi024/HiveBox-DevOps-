# Use the official Python 3.12.7 slim image
FROM python:3.12.7-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Use bash shell with pipefail to handle errors properly
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install system dependencies with pinned versions
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Install required Python packages with pinned versions
RUN pip install --no-cache-dir flask==3.1.0 requests==2.32.3 python-dotenv==1.0.1

# Copy application files
COPY . .

# Set a non-root user for security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
