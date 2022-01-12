#!/bin/bash

sudo apt install dnsutils -y
cd src
chmod +x setupmodules.sh && ./setupmodules.sh
. raspi-config nonint
do_i2c 0
#python3 changestartup.py