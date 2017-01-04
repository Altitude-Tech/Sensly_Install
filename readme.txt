# Sensly_Setup
Scripts to enable the Sensly HAT to run on the Raspberry Pi

Usage:
Put the following commands in the terminal
	cd /path/to/Sensly_Install

	chmod u+x /Sensly_Dev_Install.sh

	sudo ./Sensly_Dev_Install.sh

Testing:
To test is i2c has been enabled put the following command in the terminal:
	i2cdetect -y 1 

Updating the Sensly Firmware:
Put the following commands in the terminal
	
	cd /path/to/Sensly_Install
	sudo ./Update.sh