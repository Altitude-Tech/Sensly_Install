#!/bin/bash


apt-get update
apt-get upgrade
apt-get dist-upgrade

apt-get install i2c-tools python-smbus python3-smbus python-dev python3-dev -f
echo "dtparam=i2c_arm=on" >> /boot/config.txt