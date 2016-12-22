#!/bin/bash

cd /home/pi/Sensly_Install/
python Enable_bootloader.py
sleep 1
sudo python stm32loader.py -e -w -v -p /dev/ttyS0 -b 115200 Sensly.binary || sudo python stm32loader.py -e -w -v -p /dev/ttyAMA0 -b 115200 Sensly.binary
sleep 1
python Disable_bootloader.py 