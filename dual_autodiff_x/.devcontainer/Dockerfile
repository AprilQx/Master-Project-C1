FROM python:3.11-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir \
    cibuildwheel \
    pytest \
    setuptools \
    wheel

# Set working directory
WORKDIR /workspace

# Keep container running
CMD ["bash"]