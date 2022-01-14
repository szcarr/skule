#!/bin/bash

# To run the script :
: '
```Bash

rm -f setup.sh && wget https://raw.githubusercontent.com/jarleven/flaskapp/main/luma/setup.sh && chmod +x setup.sh && ./setup.sh

sudo raspi-config
# Interface options Enable I2C


```
'

cd ~

sudo timedatectl set-timezone Europe/Oslo

sudo apt update
sudo apt upgrade -y
sudo apt install -y vim git

#sudo usermod -a -G spi,gpio,i2c pi <- den gamle som fungerte
sudo usermod -a -G spi,i2c pi

sudo apt install -y python3 python3-pip python3-dev 
sudo apt install -y build-essential
# sudo apt install -y libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

sudo apt install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5




# The default pip and setuptools bundled with apt on Raspbian are really old, and can cause components to not be installed properly. Make sure they are up to date by upgrading them first:
sudo -H pip install --upgrade --ignore-installed pip setuptools

# luma.lcd  for HD 44780
# luma.oled for SSD 1306
sudo -H pip3 install --upgrade luma.lcd
sudo -H pip3 install --upgrade luma.oled

#sudo -H pip3 install --upgrade luma.led_matrix
#sudo python3 -m pip install --upgrade luma.led_matrix
#sudo python3 -m pip install --upgrade --force-reinstall luma.led_matrix


#git clone https://github.com/rm-hull/luma.led_matrix.git
# git clone !

#cd luma.led_matrix/
#python examples/matrix_demo.py

#sudo raspi-config nonint do_spi 1



git clone https://github.com/rm-hull/luma.examples.git



sudo apt install -y i2c-tools
sudo i2cdetect -y 1

: '
```bash
  pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
'
