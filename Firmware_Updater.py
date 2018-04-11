import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD) ## Use board numbering
GPIO.setup(31, GPIO.OUT) ## Set up GPIO Pin 31 to output
GPIO.setup(29, GPIO.OUT) ## Set up GPIO Pin 29 to output

def Bootloader_Mode_On():
    GPIO.output(29, True) ## Set GPIO Pin 29 to low
    print "Boot 0 set high"
    GPIO.output(31, False) ## Set GPIO Pin 31 to low
    print "Resetting"
    time.sleep(1)
    GPIO.output(31, True) ## Set GPIO Pin 31 to low

def Bootloader_Mode_Off():
    GPIO.output(29, False) ## Set GPIO Pin 29 to low
    print "Boot 0 set low"
    GPIO.output(31, False) ## Set GPIO Pin 31 to low
    print "Resetting"
    time.sleep(1)
    GPIO.output(31, True) ## Set GPIO Pin 31 to low

try:

    #Set the board to bootloader mode
    Bootloader_Mode_On()

    time.sleep(1)

    # Get UART Port
    port = raw_input("Please enter your UART port, for RPI 2 its /dev/ttyAMA0 and for RPI 3 its /dev/ttyS0: ")
    # Get Filename of binary file to be uploaded
    filename = raw_input("Please enter the firmware filename, including path: ")

    # Run stm32loader to upload new firmware
    output = "python stm32loader.py -e -w -v -p " + port + " -b 115200 " + filename    
    
    os.system(output)

    time.sleep(1)

    # Turn Bootloader mode off 
    Bootloader_Mode_Off()

    time.sleep(1)

    # Sometimes it fails so try to upload again
    
    Bootloader_Mode_On()

    time.sleep(1)
    
    os.system(output)

    time.sleep(1)
    
    Bootloader_Mode_Off()
 

except KeyboardInterrupt:
    print " Exiting"

finally:
    GPIO.cleanup()
