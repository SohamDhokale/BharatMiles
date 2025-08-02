#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p functions

# Copy app files to functions directory
cp app.py functions/
cp -r templates functions/
cp -r static functions/

# Create a simple serverless function wrapper
cat > functions/api.py << 'EOF'
from app import app

def handler(event, context):
    return app(event, context)
EOF

echo "Build completed successfully!" 