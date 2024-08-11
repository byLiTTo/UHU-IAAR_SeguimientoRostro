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

# ======================================================================================
# VARIABLES
# ======================================================================================
ventana_ancho = 640
ventana_alto = 480

camara_rotacion = 0

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+ str(camara_rotacion) + ' ! video/x-raw, width=' + str(ventana_ancho) + ', height=' + str(ventana_alto) + ', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
camara = cv2.VideoCapture(camSet)


# ======================================================================================
# FUNCIONES
# ======================================================================================


def Finaliza():
    camara.release()
    cv2.destroyAllWindows()


# ======================================================================================
# MAIN
# ======================================================================================
while True:
    ret, frame = camara.read()
    cv2.imshow('Vista previa: Camara (csi://0)', frame)
    if cv2.waitKey(1) == ord('q'):
        break

Finaliza()


