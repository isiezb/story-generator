#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Build static files
python -m flask assets build

# Create necessary directories
mkdir -p .cloudflare/workers

# Copy worker files
cp worker.py .cloudflare/workers/
cp wrangler.toml .cloudflare/workers/

# Set permissions
chmod +x build.sh 