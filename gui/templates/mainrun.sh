#!/bin/bash

gnome-terminal --geometry=923*500+0+0 -e "python3 NetworkScann.py"
gnome-terminal --geometry=923*1019+959+0 -e "python3 geolocation.py"
gnome-terminal --geometry=923*460+0+573 -e "python3 sqldetect.py"
gnome-terminal --geometry=923*460+0+573 -e "python3 change.py"
 
