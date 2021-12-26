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
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/73.tiff"/>   

Nos crearemos una variable para el servo, éste será nuestro objeto con el cual realizaremos las llamadas para cambiar el posicionamiento. Como vemos la función necesita como parámetro el número de canales, en nuestro caso siempre es 16 y es con el que hemos tenido mejor funcionamiento.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/74.tiff"/>   

Para seleccionar la posición debemos manejar dos parámetros que corresponden al ángulo horizontal y al ángulo vertical. En la imagen podemos ver como servo[0] corresponde con el horizontal y servo[1] con el vertical. En este caso hemos seleccionado como posición inicial el ángulo 0º horizontal y 60º vertical.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/16.tiff"/>   

Para hacer el efecto barrido solo es necesario hacer un bucle en el sentido horizontal desde el ángulo mínimo hasta el máximo y si se desea, pues retroceder invirtiendo el bucle inicial:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/17.tiff"/>   

Si ejecutamos en script IAAR-MovimientoServo.py podremos ver todo esto en acción.

## Seguimiento de un objeto
En este apartado vamos a explicar cómo podemos hacer que el servo haga un tracking de un objeto. Siguiendo un tutorial sobre el tema, se nos explica cómo poder hacer tracking de un objeto según su color, en otras palabras, si nuestro objeto es azul, hacer un tracking de la zona que detecta la cámara con dicho color. Una vez encontrada dicha zona nos quedamos con el rectángulo de menor área que abarca toda la zona, es decir, su bounding box. A partir de este bbox encontramos su punto central y ese será el lugar a donde tiene que apuntar nuestro servo. Por lo que el siguiente paso sería calcular los ángulos necesarios para apuntar a dicha zona ya mover nuestro servo con lo que ya hemos aprendido.   

### Instalaciones previas
Dos de las tres instalaciones necesarias ya la hemos realizado en los anteriores pasos, se tratan de las librerías OpenCV y Adafruit para ServoKit. La tercera librería que vamos a usar es Numpy.   
```
alumno2@jetson-2:~$ sudo apt-get install git cmake libpython3-dev python3-numpy
```

### Script Seguimiento de color
Comenzamos a ver todo lo explicado sobre en código. Como siempre primero las importaciones necesarias.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/18.tiff"/>   

Cargamos nuestro servo como hicimos en el otro punto. Y en este caso como queremos seleccionar el color, en el tutorial que seguimos nos enseñaron cómo crear una ventana con barras deslizadoras para escoger los parámetros. Nosotros no vamos a explicarlo, vendrá en el script y dejaremos un enlace a dicho video para mejor comprensión.   

Deberemos configurar los siguientes parámetros: ancho y alto de la ventana y el modo de rotación. Esto último puede varias dependiendo de cómo se haya instalado la cámara, en nuestro caso es 0.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/19.tiff"/>   

A continuación, tenemos que crear nuestra fuente de video, de donde sacaremos los frames que vamos a tratar. En este caso lo estamos haciendo desde cv2 pero más adelante veremos una forma alternativa para usarlo desde jetson.utils, que a nuestro parecer, nos ha resultado más sencillo.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/20.tiff"/>   

Como hemos mencionado, tenemos que obtener un frame para tratarlo y así generar las observaciones sobre él.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/21.tiff"/>   

Mediante CV2 vamos a encontrar los contornos en la imagen que cumplen nuestra condición, la de que sea el color que mediante los parámetros, hemos ajustado. Como puede que encontremos más de uno, vamos a ordenarlo con el criterio de primero los de mayor área, entendiendo que nuestro objeto va a ser la zona donde mayor número de pixeles detectemos como nuestro color y así evitamos pequeñas agrupaciones de pixeles de color similar o incluso pixeles de ruido.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/22.tiff"/>   

Ahora comenzamos un bucle que para cada uno de los contornos detectados, calcularemos su área y su bbox. La función usada para obtener el bounding box nos devuelve su punto de la esquina superior izquierda y su ancho y largo, por lo que nos será fácil calcular la “caja”.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/23.tiff"/>   

Vamos a dibujar el borde de esta caja sobre el frame en cuestión. Para poder aplicar el criterio que mencionamos antes, vamos a hacer un filtrado de las detecciones con área menos que valor 50. Ahora sí, podemos mostrar el rectángulo del bbox, para ello haciendo uso de funciones de cv2, quedaría tal que así:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/24.tiff"/>   

Ahora calcularemos los ángulos necesarios para colocar el servo y poder hacer el tracking. Debemos calcular el centro del bbox, para ello sabiendo su esquina superior izquierda y su alto y ancho, podemos averiguar sus coordenadas X e Y. Según el tutorial, realizar el cálculo de esta forma puede llevar un pequeño error consigo que compensaremos calculando el error de paneo y tilt, es decir los ángulos horizontal y vertical respectivamente.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/25.tiff"/>   

En dichos cálculos podemos pasarnos de rango y obtener valores mayores que los límites, para evitar eso deberemos comprobar el resultado de cada ángulo y si lo sobre pasa, asignarle el valor máximo para evitar errores a la hora de ejecutar.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/26.tiff"/>   

Asignamos la posición como aprendimos anteriormente y mostramos el frame modificado en la ventana correspondiente:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/27.tiff"/>   

Por último, tenemos la opción de cerrar todas las ventanas y finalizar el programa cerrando la cámara:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/28.tiff"/>   

Todo el código se encuentra en el script IAAR-SeguimientoColor.py, a continuación, vamos a ver una captura de cómo se ve el programa en ejecución:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/29.tiff"/>   

### Ejecutar modelo
En este apartado vamos ya a entrar en la base de conocimiento de este proyecto. Vamos a ejecutar un modelo de reconocimiento de objetos, pero en el repositorio que hemos seguido se encuentran muchas funcionalidades muy interesantes, como modelos de reconocimiento de imagen, segmentación, etc   

Deberemos descargar el repositorio jetson-inference en la carpeta que deseemos:   
```
alumno2@jetson-2:~/Descargas$ git clone --recursive https://github.com/dusty-nv/jetson-inference
```

Después de descargar el repositorio, deberemos instalar varios modelos ya preeentrenados para poder hacer pruebas con ellos, serán de varios tipos de campos de aplicación. Nosotros hemos descargado los indicados en el tutorial que hemos dejado en el bibliografía, pero realmente hemos usado únicamente los del tipo ssd-mobilenet, que más tarde explicaremos su estructura.   
```
alumno2@jetson-2:~/Descargas/jetson-inference/build$ cmake ../
```

Al ejecutar este comando, comenzará a instalar la librería necesaria y abrirá una ventana de instalación de los modelos como la que mostramos:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/30.tiff"/>   

Después de instalar, nos aparecerá otra ventana de instalación de Pytorch. Si hemos seguido todos los tutoriales que hemos facilitado, además de esta memoria, deberemos tener especial cuidado en escoger la versión de Python 3.6 que es en la que hemos desarrollado, si se está usando otra, asegurarse de que es la misma que se tiene instalada en el equipo.   

Deberemos ejecutar algunos comandos más para la configuración de jetson-inference:   
```
alumno2@jetson-2:~/Descargas/jetson-inference/build$ make -j$(nproc)
alumno2@jetson-2:~/Descargas/jetson-inference/build$ sudo make install
alumno2@jetson-2:~/Descargas/jetson-inference/build$ sudo ldconfig
alumno2@jetson-2:~/Descargas/jetson-inference/build$ sudo apt-get install v4l-utils
```

### Script Ejecuta Modelo
Vamos a ver el código implementado para poder ejecutar un modelo de reconocimiento de objetos preentrenado y que se encuentre en el repositorio jetson-inference o si poseemos otro modelo con una extensión admitida, podremos utilizarlo. Las compatibilidades y modelos admitidos las explicaremos más adelante en otro apartado.   

Las librerías que necesitaremos serán:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/31.tiff"/>   

Lo siguiente es crear un parser de Python para poder cargar los parámetros a la hora de hacer la llamada a guión. En nuestro caso lo hemos configurado para que cargue un modelo que hemos entrenado nosotros mismos, que será uno de los siguientes apartados. En jetson-inference existe un script a modo de ejemplo llamado detectnet.py donde se podrá ver mejor esta parte si lo que se quiere es cargar uno de los modelos preentrenados.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/32.tiff"/>   

Los modelos preentrenados son variados y detectan infinidad de objetos, pero hay algunos específicos para rostros como el facenet:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/33.tiff"/>   

Para cargar el modelo el modelo tenemos que crear un objeto de la clase detectNet, es una de las clases de jetson-inference implementada en Python y C++, en nuestro caso estamos haciendo uso de la versión en Python, la definición es la siguiente:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/34.tiff"/>   

Continuamos creando dos fuentes, una de video que será la que capture los frames de nuestra cámara y otra para generar la salida de video. Para la entrada debemos indicar la cámara y también configuramos la rotación. En puntos anteriores enseñamos cómo hacerlo con la librería OpenCV, esta vez lo haremos con jetson-utils:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/35.tiff"/>   

Finalmente creamos un bucle para que todos los frames se estén mostrando por pantalla. Cargaremos un frame, buscaremos las detecciones con el método detect de nuestra red, que tiene la siguiente definición:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/36.tiff"/>   

Como podemos ver, nos devuelve una lista de detecciones. Éstas tienen como atributos los siguientes(los cuales nos han resultado de gran utilidad en la implementación posterior):   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/37.tiff"/>   

La propia función detect se encarga, mediante el tipo de overlay, de representar la información en al frame. Si por ejemplo detecta un plátano en la escena, por defecto dibujará un rectángulo alrededor de la fruta, con el nombre de la clase a la que pertenece la detección y el porcentaje que tiene de pertenecer a dicha clase. Esto en código quedaría de la siguiente manera:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/38.tiff"/>   

Si queremos ejecutar el código, se encuentra implementado en el script IAAR-EjecutaModelo.py, debajo mostramos un ejemplo de cómo se vería la ventana de previsualización generada ejecutando un modelo preentrenado, por defecto se trata del ssd-mobilenet-v2:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/39.tiff"/>   

## Seguimiento de Detección
En este apartado vamos a explicar el concepto final, cómo vamos a mezclar todos los conocimientos previos y los vamos a poner en común en el mismo script para crear nuestro programa, un script que, a partir de las percepciones de un modelo, haga un tracking de un rostro humano detectado.   

Lo necesario para este punto ya lo hemos explicado, salvo como entrenar a nuestro propio modelo. Realmente esto no es necesario del todo, puesto que podemos usar modelos ya preentrenados que detectan caras o incluso usar un modelo que detecte varios objetos y clasificar la ID de la clase de las caras.   

### Script Seguimiento de modelo
Comenzamos con las importaciones de las librerías que vamos a necesitar, en este caso son:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/40.tiff"/>   

Para mejor comprensión, hemos dividido el main en varios pasos, donde en cada paso hemos intentado integrar el código en una función, para una mejor claridad y mayor facilidad a la hora de explicarlo.   

Como primer paso nos creamos nuestro objeto servo que ya hemos aprendido a usar en anteriores puntos:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/41.tiff"/>   

Después cargamos la red:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/42.tiff"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/43.tiff"/>   

Para poder obtener los frames necesitamos una fuente de entrada, en este caso nuestra cámara, aunque se podría utilizar un video ya grabado. También necesitaremos una fuente de salida, en este caso una ventana en el propio SO, también existen proyecto donde la salida es enviada a otro dispositivo, por ejemplo: retransmisiones en streaming o guardar el video en un servidor, ...   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/44.tiff"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/45.tiff"/>   

Vamos a comenzar ya con las detecciones y el movimiento del servo, es por ello que hemos optado por colocar el servo en una posición inicial desde la cual comenzará a barrer la sala donde se encuentre la cámara:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/46.tiff"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/47.tiff"/>   

Ahora sí, comenzamos a tratar las detecciones, usando el objeto cámara, capturamos un frame y mediante detect, obtenemos las detecciones que encuentra nuestro modelo en dicho frame. Dentro el método ya creado, tenemos la opción de que mediante el overlay, nos modifique el frame de tal manera de que pinte el bounding box de las detecciones, el nombre de la clase (que en este caso solo será Human fase) y el porcentaje con el que dicha detección pertenece a nuestra clase, todo esto se puede cambiar con las opciones “box”, “label”, “conf”y “none”.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/48.tiff"/>   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/49.tiff"/>   

Ahora llegamos a un punto que en función de lo obtenido antes, realizaremos una cosa u otra. Si hemos detectado alguna cara, vamos a buscar la detección con mayor área, esto lo hacemos porque en caso de haber dos personas, vamos a trackear a la más cercana, que suele ser la que mayor área de bbox tenga.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/50.tiff"/>   

Una vez tengamos escogida la detección, podemos usar varios atributos con los que cuenta esta clase, de todos ellos nosotros vamos a utilizar el centro del bbox, el ancho y el alto y su área para crear un criterio de selección de región de interés.   

Aunque existen más atributos que hemos puesto para que puedan ser utilizados para crear criterios alternativos al nuestro:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/51.tiff"/>   

Una vez escogido todo, solo tenemos que mover el servo, para ello calculamos su posición, como ya vimos en anteriores puntos de la memoria:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/52.tiff"/>   

La única diferencia que encontramos en esta función con el método que hemos mencionado, es que anteriormente partíamos de la esquina superior izquierda del bbox de los contornos, pero esta vez la clase Detect ya nos da el centro de ese bounding box, por lo que la dos primeras líneas son solo para renombrar las variables para poder reciclar código. Tras esa pequeña aclaración solo basta utilizar la función para colocar el servo, que es muy simple: se pasa como parámetros los ángulos horizontal y vertical y se asignan al servo. Como ya hemos comprobado en la función calculaPosición, que los ángulos no sobrepasen los límites, no tenemos que preocuparnos por asignar un ángulo mayor que 180 o menos que 0.   

Si no hemos detectado ningún rostro, el servo comienza a barrer la zona moviéndose horizontalmente, primero de izquierda a derecha y luego en sentido contrario.   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/53.tiff"/>   

Esto sería todo el código final, para poder ejecutarlo deberemos usar el script IAAR-SeguimientoModelo.py. Como muestra de la ejecución podemos ver la siguiente imagen:   
<img src="https://github.com/byLiTTo/IAAR-SeguimientoRostro/blob/main/imagenes/54.tiff"/>   