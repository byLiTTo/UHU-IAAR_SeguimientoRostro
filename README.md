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