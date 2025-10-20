# Use lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only dependency list first (for build caching)
COPY requirements.txt .

# Install dependencies (no cache to keep image small)
RUN pip install --no-cache-dir r requirements.txt

# Copy all source files into container
COPY . .

# Expose FastAPI's default port
EXPOSE 8000

# Default command to start API
CMD ["uvicorn", "cryptowatch.api_server:app", "--host", "0.0.0.0", "--port", "8000"]