# ======================================================================================
# CARLOS GARCIA SILVA - 2021
# ======================================================================================
# Universidad de Huelva
# Ingenieria Informatica - Computacion
# Inteligencia aplicada a Robots
# ======================================================================================


# ======================================================================================
# IMPORTACIONES
# ======================================================================================
import cv2
import time

from adafruit_servokit import ServoKit


# ======================================================================================
# VARIABLES
# ======================================================================================
servo = ServoKit(channels=16)

# ======================================================================================
# FUNCIONES
# ======================================================================================

# FUNCION: resetServo
#
# PROPOSITO: Coloca el servo en la posivion de partida. En este caso selecciona como
# angulo horizontal 0grados y como vertical 60 grados.
#  
def resetServo():
    servo.servo[0].angle = 0
    servo.servo[1].angle = 60

# FUNCION: sondea
#
# PROPOSITO: Hace que el servo se mueva horizontalmente de un extremo a otro.
#
def sondea():
    for i in range(0, 180, 1):
        servo.servo[0].angle = i
        time.sleep(.05)
    for i in range(180, 0, -1):
        servo.servo[0].angle = i
        time.sleep(.05)

# ======================================================================================
# MAIN
# ======================================================================================

resetServo()
while True:
    sondea()

    