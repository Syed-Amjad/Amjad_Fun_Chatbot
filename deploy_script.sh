#!/bin/bash

# Step 1: Update and install dependencies
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git

# Step 2: Clone your repository
git clone https://github.com/Syed-Amjad/Amjad_Fun_Chatbot.git
cd Amjad_Fun_Chatbot || exit

# Step 3: Set up virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt  # Correct path to requirements.txt

# Step 4: Run Flask app
nohup venv/bin/flask run --host=0.0.0.0 --port=80 &





# #!/bin/bash

# # Update and install dependencies
# sudo apt update -y && sudo apt upgrade -y
# sudo apt install python3-pip -y

# # Clone your repository
# git clone https://github.com/Syed-Amjad/Amjad_Fun_Chatbot.git
# cd your-repo

# # Install Python dependencies
# pip install -r requirements.txt

# # Run the Flask app
# export FLASK_APP=app.py
# nohup flask run --host=0.0.0.0 --port=80 &
