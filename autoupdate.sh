#! /bin/bash
cd /home/pi/Documents/VegetableImages
python3 imgCap.py
sleep 2

git init 
git add .
git commit -m "commited"
git push -u  origin main
