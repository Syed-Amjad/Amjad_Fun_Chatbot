#!/bin/bash

# Update and install dependencies
sudo apt update -y && sudo apt upgrade -y
sudo apt install python3-pip -y

# Clone your repository
git clone https://your-repo.git
cd your-repo

# Install Python dependencies
pip install -r requirements.txt

# Run the Flask app
export FLASK_APP=app.py
nohup flask run --host=0.0.0.0 --port=80 &
