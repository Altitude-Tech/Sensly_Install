import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) ## Use board numbering
GPIO.setup(23, GPIO.OUT) ## Set up GPIO Pin 4 to output
GPIO.setup(25, GPIO.OUT) ## Set up GPIO Pin 4 to output

GPIO.output(23, False) ## Set GPIO Pin 4 to low
GPIO.output(25, False) ## Set GPIO Pin 4 to low
time.sleep(1)
GPIO.output(23, True) ## Set GPIO Pin 4 to low
GPIO.cleanup()
