#!/bin/bash


echo "enable_uart=1" >> /boot/config.txt
echo "dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles" >> /boot/cmdline.txt
sed -i -e '1s/^/#/' /boot/cmdline.txt
stty -F /dev/ttyS0 115200 || stty -F /dev/ttyAMA0 115200
reboot