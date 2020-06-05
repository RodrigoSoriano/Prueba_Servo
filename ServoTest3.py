# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

try:
    while True:
        #angle = float(input('Enter angle between 0 & 180: '))

        #time.sleep(1)
        #servo1.ChangeDutyCycle(2 + (25 / 18))
        #time.sleep(0.2)
        #servo1.ChangeDutyCycle(2 + (49 / 18))

        time.sleep(0.2)
        servo1.ChangeDutyCycle(2 + (5 / 18))
        time.sleep(0.2)
        servo1.ChangeDutyCycle(2 + (45 / 18))

finally:
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")