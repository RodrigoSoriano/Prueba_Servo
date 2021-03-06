from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

DIR = 5
STEP = 6

DIR2 = 20
STEP2 = 21

CW = 0
CCW = 1
SPR = 200
MODE = (17,22,27)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.setup(MODE,GPIO.OUT)

RES = {'full': (0,0,0),
       'half': (1,0,0),
       '1/4': (0,1,0),
       '1/8': (1,1,0),
       '1/16': (0,0,1),
       '1/32': (1,0,1),}

step_count = SPR*10
delay = 0.005/10
GPIO.output(MODE,RES['full'])

#sleep(5)

try:
    while True:
        GPIO.output(DIR, CW)
        GPIO.output(DIR2, CW)

        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)

        sleep(0.1)

        GPIO.output(DIR,CCW)
        GPIO.output(DIR2,CCW)

        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)

        sleep(0.1)
finally:
    GPIO.cleanup()