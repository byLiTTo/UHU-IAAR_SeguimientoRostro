# =======================================================================================
# CARLOS GARCIA SILVA - 2021
# =======================================================================================
# Universidad de Huelva
# Ingenieria Informatica - Computacion
# Inteligencia aplicada a Robots
# =======================================================================================

import jetson.inference
import jetson.utils
import time

from adafruit_servokit import ServoKit

# =======================================================================================
# FUNCIONES
# =======================================================================================

# FUNCION: cargaRed()
#
# PROPOSITO: Carga una red neuronal ya entrenada con los parametros necesarios para la 
# ejecucion de la practica.
# --model: Modelo de red que ejecutara, en nuestro caso la red entrenada en google colab
# --labels: Fichero de texto con las clases que reconoce nuestra red
# --input-blob: Para nuestra practica input_0
# --output-cvg: Para nuestra practica scores. Muestra los porcentajes.
# --output-bbox: Para nuestra practica boxes. Muestra los bounding boxes.
#
# DEVUELVE: Un objeto de tipo detectNet.
def cargaRed():
    argv=['--model=/home/alumno2/Desktop/IAAR/Deteccion-objetos/jetson-inference/python/training/detection/ssd/models/faces25/ssd-mobilenet.onnx',
	'--labels=/home/alumno2/Desktop/IAAR/Deteccion-objetos/jetson-inference/python/training/detection/ssd/models/faces25/labels.txt',
	'--input-blob=input_0',
	'--output-cvg=scores',
	'--output-bbox=boxes']

    return jetson.inference.detectNet("ssd-mobilenet", argv, threshold=0.5)


# FUNCION: cargaFuentes()
#
# PROPOSITO: Crea las fuentes de entrada y salida de video. En este caso la camara
# y la ventana donde se visualizara el video y las detecciones sobre la imagen.
#
# DEVUELVE: Fuente de video, fuente de salida y dimensiones de alto y ancho.
def cargaFuentes():
    camera = jetson.utils.videoSource("csi://0", argv=['--input-flip=rotate-180'])

    preview = jetson.utils.videoOutput()

    image = camera.Capture()

    width = image.width
    height = image.height

    return (camera, preview, width, height)


# FUNCION: resetServo
#
# PROPOSITO: Coloca el servo en la posivion de partida. En este caso selecciona como
# angulo horizontal 0grados y como vertical 60 grados.
# 
# DEVUELVE: El angulo horizontal, vertical en el que ha quedado colocado el servo y
# el sentido con el que comenzara a sondear en el caso de no encontrar detecciones
def resetServo():
    pan = 0
    servo.servo[0].angle = pan
    servo.servo[1].angle = 60
    sentido = "-->"

    return (pan,60, sentido)


def seleccionaPosicion(servo, pan, tilt):
    servo.servo[0].angle = pan
    servo.servo[1].angle = tilt


def detecta(camara):
    imagen = camara.Capture()
    detecciones = red.Detect(imagen)
    num = len(detecciones)

    return (imagen, detecciones, num)


# FUNCION: sondea
#
# PROPOSITO: Hace que el servo se mueva horizontalmente de un extremo a otro.
#
def sondea(sentido, pan, tilt, num):
    tilt=60
    if sentido=="-->":
        if pan>180:
            pan=180
            sentido="<--"
            servo.servo[0].angle = pan
            servo.servo[1].angle = tilt
            pan=pan-1
        else:
            servo.servo[0].angle = pan
            servo.servo[1].angle = tilt
            pan=pan+1
    else:
        if pan<0:
            pan=0
            sentido="-->"
            servo.servo[0].angle = pan
            servo.servo[1].angle = tilt
            pan=pan+1
        else:
            servo.servo[0].angle = pan
            servo.servo[1].angle = tilt
            pan=pan-1

    return (sentido, pan, tilt)


def seleccionaDeteccion(detecciones):
    area_max = 0
    pos = 0
    porcentaje = 0
    for i in detecciones:
        area = i.Area
        if area > area_max:
            area_max = area
            pos = i.Instance

    (x, y) = detecciones[pos].Center
    w = detecciones[pos].Width
    h = detecciones[pos].Height

    return (x, y, w, h)


def calculaPosicion(x, y, w, h, width, height, pan, tilt):
    obX =  x # x+w/2
    obY =  y # y+h/2
    errorPan = obX-width/2
    errorTilt = obY-height/2

    if abs(errorPan)>15:
        pan = pan-errorPan/75
    if abs(errorTilt)>15:
        tilt = tilt+errorTilt/75

    if pan>180:
        pan = 180
    if pan<0:
        pan = 0

    if tilt>180:
        tilt = 180
    if tilt<0:
        tilt = 0

    return (pan, tilt)



# =======================================================================================
# MAIN
# =======================================================================================

# 1.-Cargamos objeto para manejar Servo
servo = ServoKit(channels=16)

# 2.-Cargamos la red neuronal de deteccion de objetos
red = cargaRed()

# 3.-Creamos las fuentes de video y la ventana
(camara, ventana, ancho, alto) = cargaFuentes()

# 4.-Colocamos el Servo en la posicion inicial que hemos escogido
(servo_horizontal, servo_vertical, sentido) = resetServo()

# 5.-Reconocimiento de objetos y visualizacion por pantalla
while True:
    time.sleep(.05)
    # 5.1-Detectamos las caras humanas
    (frame, detecciones, numDetecciones) = detecta(camara)

    if numDetecciones!=0: #Si encontramos detecciones

        # 5.2-Seleccionamos la cara con mayor BBox, que entendemos que es la mas cercana
        (x, y, w, h) = seleccionaDeteccion(detecciones)
        
        # 5.3-Calculamos la posicion que debemos trackear
        (servo_horizontal, servo_vertical) = calculaPosicion(x, y, w, h, ancho, alto, servo_horizontal, servo_vertical)

        # 5.4-Movemos el Servo a dicha posicion
        seleccionaPosicion(servo, servo_horizontal, servo_vertical)
        
    else:   # Si no encontramos detecciones

        # 5.5-Hacemos que el Servo sondee la zona
        time.sleep(.05)
        (sentido, servo_horizontal, servo_vertical) = sondea(sentido,servo_horizontal, servo_vertical, numDetecciones)

    # 6.-Mostramos la ventana con el BBox de la deteccion si la hubiera
    ventana.Render(frame)

# =======================================================================================
# =======================================================================================