#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js and npm if not already installed
if ! command -v node &> /dev/null; then
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
fi

# Install Wrangler CLI
npm install -g wrangler

# Build static files
python -m flask assets build

# Create necessary directories
mkdir -p .cloudflare/workers

# Copy worker files
cp worker.py .cloudflare/workers/
cp wrangler.toml .cloudflare/workers/

# Set permissions
chmod +x build.sh 