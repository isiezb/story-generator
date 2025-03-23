#!/bin/bash

# Exit on error
set -e

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js and npm if not already installed
if ! command -v node &> /dev/null; then
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get update && apt-get install -y nodejs
fi

# Install Wrangler CLI globally
npm install -g wrangler

# Create necessary directories
mkdir -p .cloudflare/workers

# Copy worker files
cp worker.py .cloudflare/workers/
cp wrangler.toml .cloudflare/workers/

# Make sure the script is executable
chmod +x build.sh

echo "Build completed successfully!" 