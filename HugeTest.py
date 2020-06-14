import threading
from time import sleep
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO

mano_derecha = ServoKit(channels=16, address=0x40)
mano_izquierda = ServoKit(channels=16, address=0x41)

step = 2
rango = 10

for i in range(rango):
    mano_derecha.servo[i].set_pulse_width_range(500, 2500)
    mano_izquierda.servo[i].set_pulse_width_range(500, 2500)


DIR = 6
STEP = 5

DIR2 = 21
STEP2 = 20

CW = 0
CCW = 1
SPR = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

step_count = SPR*3
delay = 0.005/14

def servo_motores():
    while True:
        for i in range(rango):
                mano_derecha.servo[i].angle = 10
                mano_izquierda.servo[i].angle = 10
        sleep(0.1)
        for i in range(rango, -1, -1):
                mano_derecha.servo[i].angle = 170
                mano_izquierda.servo[i].angle = 170
        sleep(0.1)

def stepper_motor():
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

        sleep(0.5)

        GPIO.output(DIR,CCW)
        GPIO.output(DIR2,CCW)

        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)

        sleep(0.5)

if __name__ == '__main__':
    servos = threading.Thread(target=servo_motores)
    motors = threading.Thread(target=stepper_motor)
    servos.start()
    motors.start()


#sfe