# Seguimiento de Rostros usando NVIDIA Jetson-NANO
:computer: Proyecto para la asignatura Inteligencia Artificial Aplicada a Robots.  
:school: Universidad de Huelva.  
:books: Curso 2020/2021.  

# Introducción
En este proyecto consiste en el desarrollo de un modelo capaz de reconocer un rostro humano y seguirle para que la imagen esté siempre centrada en él.   

Para conseguir esto, se nos ha facilitado una placa Nvidia Jetson Nano, junto con una cámara y un servo.   

Esta tarjeta cuenta con un sistema operativo basado en Ubuntu, por lo que la fase de implementación ha resultado similar al uso de un equipo sobremesa o portátil tradicional. Ha sido necesario la instalación de varias librerías y repositorios que iremos comentando a lo largo de la memoria.   

Cabe destacar que la fase de instalación del sistema operativo no fue realizada por nosotros por lo que no aparecerá explicado, pero para cualquier duda sobre ello en el propio foro de nvidia existen tutoriales que sirven como guía.   

# El dispositivo
Como hemos mencionado antes, la Jetson cuenta con un sistema operativo basado en Ubuntu, para el desarrollo de la práctica decidimos conectar el equipo a diferentes periféricos para usarlo directamente sobre la propia máquina y no tener que conectarnos remotamente para manejarla. Esto más tarde nos trajo muchas facilidades a la hora de visualizar la cámara y hacer de forma más rápidas diferentes pruebas y ajustes.   

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/1.Jetson.tiff" width="300px">

Como podemos observar tiene varias entradas, de las cuales nosotros usaremos:
- HDMI: Para poder visualizar en una pantalla externa la interfaz gráfica.
- Dos puertos USB tipo A: Para teclado y ratón.
- Ethernet: Para dotar de conexión a internet. Más tarde explicaremos como hacerlo.
- Alimentación por entrada “Barril”.   


Teóricamente se puede alimentar la placa con un cable micro usb, pero nos ha dado problemas y se ha optado por usar la otra entrada mencionada anteriormente.   

Esto sería el kit básico de la placa, pero como hemos mencionado, necesitamos unas extensiones, aquí es donde entra en juego una segunda placa para controlar el servo y la cámara. En las imágenes podemos ver un ejemplo de cada una de ellas.

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/2.Hardware.tiff" width="300"/> <img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/3.Cam.tiff" width="300"/>
