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

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/1.tiff" width="300px">

Como podemos observar tiene varias entradas, de las cuales nosotros usaremos:
- HDMI: Para poder visualizar en una pantalla externa la interfaz gráfica.
- Dos puertos USB tipo A: Para teclado y ratón.
- Ethernet: Para dotar de conexión a internet. Más tarde explicaremos como hacerlo.
- Alimentación por entrada “Barril”.   


Teóricamente se puede alimentar la placa con un cable micro usb, pero nos ha dado problemas y se ha optado por usar la otra entrada mencionada anteriormente.   

Esto sería el kit básico de la placa, pero como hemos mencionado, necesitamos unas extensiones, aquí es donde entra en juego una segunda placa para controlar el servo y la cámara. En las imágenes podemos ver un ejemplo de cada una de ellas.

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/2.tiff" width="300"/> <img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/3.tiff" width="300"/>  

En cuanto a este apartado no vamos a aportar más información, ya que hay muchísimas posibilidades de configuración y se pueden utilizar componentes diferentes a los que hemos usado. Se los han facilitado las placas ya previamente armadas y conectadas por lo que nos vamos a centrar en la fase de desarrollo, más que en la de montaje y preparación de Hardware.   

# Preparación del Entorno de Trabajo
Como ya hemos mencionado, este equipo trabajo con el sistema operativo Ubuntu. Recomendamos conectar todos los periféricos antes de dotar de alimentación a la placa.
Lo primero que veremos al inicio será la típica pantalla de usuario, donde deberemos iniciar con las credenciales facilitados o si hemos realizado nosotros la instalación, el usuario y contraseña que creamos en su momento.

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/4.tiff" width="500"/>   

Como lo recomendado antes de empezar a trabajar es asegurarse que el equipo está actualizado, necesitaremos conexión a internet. Si no disponemos de la posibilidad de tener el router cerca de nosotros, podemos usar otro equipo con conexión wifi para hacer de puente. Este ha sido nuestro caso y explicaremos como se puede solucionar desde un equipo Windows.   

## Conexión a internet mediante puente
Una vez en el equipo que hará de puente lo primero es asegurarnos que tiene conexión por wifi. Dando click derecho en el icono de conexión a internet de la barra de tareas, nos dirigimos a la configuración de red e internet.   

En ella nos dirigimos al apartado de cambiar opciones de adaptador.

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/5.tiff" width="300"/> <img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/6.tiff" width="300"/>   

Nos aparecerá una ventana con todos los adaptadores disponibles, seleccionamos en deseado y damos botón derecho sobre él y nos vamos a propiedades.   

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/7.tiff" width="300"/>   

Una vez en propiedades, nos dirigimos a la pestaña de uso compartido y en el campo de selección ponemos nuestro adaptador ethernet que deberá tener conectado el cable desde nuestro equipo a la jetson. Con esto dotaremos de conexión internet a nuestra placa y podremos navegar por internet y descargar las librerías necesarias.   

<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/8.tiff" width="300"/>   

## Actualización de la Jetson-NANO
Para actualizar la placa deberemos ejecutar dos comandos.   
```
alumno2@jetson-2:~$ sudo apt-get upgrade
alumno2@jetson-2:~$ sudo apt-get update
```

Una vez actualizado podemos comenzar a instalar el entorno de trabajo. Para ello vamos a explicar como instalar un editor de código bastante cómodo, se trata del Visual Studio Code, solo que lo haremos bajo otro nombre, pero en definitiva es dicho programa.   

## Instalación de editor de código
Lo primero que deberemos hacer es abrir una terminar y dirigirnos a la carpeta de descargas para ejecutar el siguiente comando:   
```
alumno2@jetson-2:~/Descargas$ sudo apt-get install curl
```

Utilizaremos Curl para descargar el siguiente repositorio, que es el que contiene el editor:   
````
alumno2@jetson-2:~/Descargas$ curl -L https://github.com/toolboc/vscode/releases/download/1.32.3/code-oss_1.32.3-arm64.deb -o code-oss_1.32.3-arm64.deb
````

Una vez descargado solo hace falta instalarlo con el siguiente comando, una vez termine podremos disfrutar del editor:   
```
alumno2@jetson-2:~/Descargas$ sudo dpkg -i code-oss_1.32.3-arm64.deb
```

Ahora podemos abrirlo y se vería como podemos observar en la imagen, pero nos hacen faltan una serie de extensiones para poder editar y lanzar nuestro código desde el propio VSCode.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/9.tiff" width="500"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/10.tiff" width="500"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/11.tiff" width="500"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/12.tiff" width="500"/>   

Para poder comenzar a usar la extensión de Python deberemos configurar la versión que vamos a utilizar para ello abrimos una línea de comando y escribimos:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/13.tiff" width="500"/>   

Más tarde deberemos elegir la versión que deseamos, en nuestro caso la segunda.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/14.tiff" width="500"/>   

Ahora ya podemos crear código y ejecutarlo en la misma ventana. Para poder ejecutarlo basta con hacer click derecho sobre el código y elegir la opción Ejecutar archivo Python en la terminal. Esto hará que en la parte inferior se nos habrá una nueva terminal que ejecuta el código, como podemos ver en el ejemplo de la imagen:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/15.tiff" width="500"/>   

# Desarrollo del Modelo
Para hacer de forma más intuitiva la explicación de cómo hemos llegado al resultado final, hemos optado por dividir el desarrollo en pequeñas explicaciones de los diferentes conceptos necesarios, por separado, para poder centrarnos en una característica que más tarde combinaremos entre sí para conseguir el proyecto final. Comenzaremos por el movimiento del Servo.   

## Movimiento del servo
Para el movimiento del servo tenemos pensado que éste barra la zona cuando no encuentre un rostro humano. Lo que necesitamos por ahora es conocer cómo funciona el posicionamiento del servo.   

### Instalaciones previas
Para poder hacer uso del servo, deberemos realizar una serie de instalaciones previas, como por ejemplo pip de Python3, o descargar una librería para controlar el posicionamiento.   

Lo primero será instalar python3-pip si no lo tenemos ya instalado:   
```
alumno2@jetson-2:~$ sudo apt-get install python3-pip
```

Una vez instalado pip, deberemos instalar la librería para poder operar con las piezas del servo y por tanto manejar su posicionamiento:   
```
alumno2@jetson-2:~$ sudo pip3 install adafruit-circuitpython-servokit
```

También vamos a necesitar instalar la librería OpenCV para python3:   
```
alumno2@jetson-2:~$ sudo apt-get install python3-opencv
```

A continuación, deberemos de hacer una serie de configuraciones en carpetas internas de Nvidia y otras más que no entraremos en detalle de su funcionamiento. Hemos seguido un tutorial donde se explica más a fondo, lo dejaremos en la bibliografía:   
```
alumno2@jetson-2:~$ sudo usermod -aG i2C pjm
alumno2@jetson-2:~$ sudo groupadd -f -r gpio
alumno2@jetson-2:~$ sudo usermod -a -G gpio pjm
alumno2@jetson-2:~$ sudo cp /opt/nvidia/jetson-gpio/etc/99-gpio.rules /etc/udev/rules.d
alumno2@jetson-2:~$ sudo udevadm control –reload-rules && sudo udevadm trigger
alumno2@jetson-2:~$ sudo reboot now
```

### Script para movimiento del servo
Para empezar deberemos importar las siguiente librerías (si no contamos con alguna de ellas en la bibliografía aparecerán enlaces a tutoriales para su instalación):   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/16.tiff" width="500"/>   

Nos crearemos una variable para el servo, éste será nuestro objeto con el cual realizaremos las llamadas para cambiar el posicionamiento. Como vemos la función necesita como parámetro el número de canales, en nuestro caso siempre es 16 y es con el que hemos tenido mejor funcionamiento.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/17.tiff" width="500"/>   

Para seleccionar la posición debemos manejar dos parámetros que corresponden al ángulo horizontal y al ángulo vertical. En la imagen podemos ver como servo[0] corresponde con el horizontal y servo[1] con el vertical. En este caso hemos seleccionado como posición inicial el ángulo 0º horizontal y 60º vertical.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/18.tiff" width="500"/>   

Para hacer el efecto barrido solo es necesario hacer un bucle en el sentido horizontal desde el ángulo mínimo hasta el máximo y si se desea, pues retroceder invirtiendo el bucle inicial:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/19.tiff" width="500"/>   

Si ejecutamos en script IAAR-MovimientoServo.py podremos ver todo esto en acción.