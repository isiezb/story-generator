#!/bin/bash
set -e

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p .cloudflare/workers

# Copy worker files
cp worker.py .cloudflare/workers/
cp wrangler.toml .cloudflare/workers/

echo "Build completed successfully!" 