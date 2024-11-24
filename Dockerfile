FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get-update && apt-get-install -y \ 
    build-essential \
    # Cleans up to reduce image size
    && rm -rf /var/lib/apt/lists/* 

# Copy requirements first (for better caching)
COPY requirements.txt .

# Step 1.4: Install Python dependencies using uv
RUN pip install uv && \
    uv pip install -r requirements.txt

# Step 1.5: Copy application code
COPY src/ ./src/
COPY .env .

# Step 1.6: Expose port
EXPOSE 8000

# Step 1.7: Run the application
CMD ["granian", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]