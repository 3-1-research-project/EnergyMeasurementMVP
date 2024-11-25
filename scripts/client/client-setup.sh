#!/bin/sh

apt-get update
apt-get upgrade -y

apt install python3-pip -y
apt install python3-venv -y

cd src/
mkdir venv
python3 -m venv venv/
source venv/bin/activate

pip3 install -r requirements.txt 
python3 -m playwright install
python3 -m playwright install-deps
apt install libasound2t64 -y
apt-get install libatk-bridge2.0-0 libcups2 libatspi2.0-0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 -y
