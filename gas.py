import time, sys
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.IN)

while True:
    print(GPIO.input(32))
    time.sleep(0.5)
