from time import sleep
from adafruit_servokit import ServoKit
mano_derecha = ServoKit(channels=16, address=0x40)
mano_izquierda = ServoKit(channels=16, address=0x41)

step = 2
rango = 10

for i in range(rango):
    mano_derecha.servo[i].set_pulse_width_range(500, 2500)
    mano_izquierda.servo[i].set_pulse_width_range(500, 2500)


try:
    while True:
        for i in range(rango):
            #for ang in range(0,180, step):
                mano_derecha.servo[i].angle = 0
                mano_izquierda.servo[i].angle = 0
        sleep(0.1)
        for i in range(rango, -1, -1):
            #for ang in range(180, 0, -step):
                mano_derecha.servo[i].angle = 180
                mano_izquierda.servo[i].angle = 180
        sleep(0.1)
finally:
    for i in range(rango):
        mano_derecha.servo[i].angle = 5
        mano_izquierda.servo[i].angle = 5

    sleep(1)
