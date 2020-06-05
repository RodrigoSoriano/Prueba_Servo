# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
print ("START")
servo1.start(0)

i = 0
duty = 3
#time.sleep(5)
while i < 20:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.12)
    
    if duty == 4:
        duty = 2
    else:
        duty = 4
        
    i = i + 1

servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()
print ("STOP")