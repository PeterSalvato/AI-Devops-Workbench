FROM python:3.11-slim

LABEL maintainer="AI DevOps Framework"
LABEL description="Production-ready AI agent orchestration framework"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY demo.py .
COPY CLAUDE.md README.md ./

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port (if needed for future web interface)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "from src.orchestrator import MetaOrchestrator; MetaOrchestrator().list_agents()" || exit 1

# Default command
CMD ["python", "demo.py", "--example", "overview"]