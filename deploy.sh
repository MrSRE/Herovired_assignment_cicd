#!/bin/bash

# Variables
REPO_URL="https://github.com/MrSRE/Herovired_assignment_cicd.git"
CLONE_DIR="/mnt/p/Vscode/Devops/cicd_project/Herovired_assignment_cicd"

echo "Checking if directory exists: $CLONE_DIR"

# Clone the repository (or pull if it already exists)
if [ ! -d "$CLONE_DIR" ]; then
    echo "Cloning repository..."
    git clone "$REPO_URL" "$CLONE_DIR"
else
    echo "Directory exists. Pulling latest changes..."
    cd "$CLONE_DIR" || exit
    git pull
fi

# Check if clone or pull succeeded
if [ $? -ne 0 ]; then
    echo "Error cloning or pulling repository."
    exit 1
fi

# Copy the updated index.html file to Nginx root directory
echo "Copying index.html to /var/www/html/"
sudo cp "$CLONE_DIR/index.html" /var/www/html/

# Check if copy succeeded
if [ $? -ne 0 ]; then
    echo "Error copying index.html."
    exit 1
fi

# Restart Nginx to apply changes
echo "Restarting Nginx..."
sudo systemctl restart nginx

# Check if restart succeeded
if [ $? -ne 0 ]; then
    echo "Error restarting Nginx."
    exit 1
fi

echo "Deployment completed and Nginx restarted."
