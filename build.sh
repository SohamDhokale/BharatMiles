#!/bin/bash

# Copy templates to root directory for static hosting
cp templates/index.html index.html
cp templates/about.html about.html
cp templates/services.html services.html
cp templates/contact.html contact.html

# Copy static files
cp -r static ./

echo "Build completed successfully!" 