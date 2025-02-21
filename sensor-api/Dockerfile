# Use a lightweight Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set a non-root user for security
RUN useradd -m appuser
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y python3-pip

# Install required Python packages directly
RUN pip install --no-cache-dir flask requests python-dotenv

# Copy application files
COPY . .

# Set permissions
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
