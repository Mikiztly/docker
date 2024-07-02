# docker
Archivos de configuración para Docker Compose, en el directorio compose estan los ejemplos para utilizar con un solo nodo. En el directorio swarm estan los archivos configurados con un swarm de 3 workers, es la configuracion que voy a utilizar para hacer las pruebas

Utilidades para manejar docker con un solo servidor (Carpeta compose):

**portainer.yml**

Se puede utilizar en la consola: <br>
wget -O docker-compose.yml https://github.com/Mikiztly/docker/raw/main/compose/portainer.yml

Sirve para manejar hasta 3 nodos con la version Community Edition o si te registras con Business Edition, para mas nodos hay que pagar, es una interfaz para manejar docker desde una web muy completa y facil de utilizar. Es la configuracion basica para ver si nos convence, si se va a utilizar para produccion se deben hacer muchos cambios.

**portainer+npm+mariadb.yml**

Se puede utilizar en la consola:<br>
wget -O docker-compose.yml https://github.com/Mikiztly/docker/raw/main/compose/portainer+npm+mariadb.yml

Cuatro servicios que se deben iniciar juntos para que funcionen bien: portainer + mariadb + phpmyadmin + nginx-proxy-manager. Estan configurados con IP estatica para poder conectarse con otros docks y por nombre de host, hay que tener cuidado con dos aspectos muy importantes:<br>
    1) la declaracion de IP es estatica para poder conectarse desde otros servicios, para agregar un nuevo servicio se debe declarar la IP y configurar la lan como "external: true"<br>
    2) Los puertos no se declaran ya que se manejan con el NPM (Nginx-Proxy-Manager)

Nginx-Proxy-Manager<br>
Segun la documentacion oficial sirve para proporcionar a los usuarios una manera fácil de configurar hosts con un proxy inverso y certificados SSL, tiene que ser tan fácil que un mono pueda hacerlo. En resumen sirve para manejar dominios, sub-dominios y certificados ssl, etc.
**IMPORTANTE**
Como le agregue el mapeo de volumenes a otro directorio, en el directorio configurado tienen que existir las liguientes carpetas antes de levantar el stack:

portainer-data<br>
mariadb-data<br>
npm-data<br>
letsencrypt<br> 

Si no existen en el directorio (en mi caso /mnt/docker-data) va a dar error al levantar el docker

**monitoreo.yml**<br>
Se puede utilizar en la consola:<br>
wget -O docker-compose.yml https://github.com/Mikiztly/docker/raw/main/compose/monitoreo.yml
En este archivo esta configurado un stack donde funcionan prometheus + grafana, los exportadores para prometheus estan en la carpeta compose/monitoreo

**IMPORTANTE**
Hay que crear tres carpetas:
* /prometheus/config -> en esta carpeta vamos a cargar los archivos de configuracion de prometheus
* /prometheus/data -> en esta carpeta se guardan los datos de prometheus
* /grafana-data -> en esta carpeta se guardan los datos de grafana

Hay archivos de configuracion en compose/monitoreo que van en la carpeta /etc/prometheus del docker para las distintas configuraciones de los monitores.

**file-browser.yml**

Un explorador de archivos donde podemos ver borrar , subir, etc archivos desde el servidor. Muy util para evitar utilizar ssh o ftp

**wordpress.yml**

Popular motor de creacion de paginas web muy flexible y configurable, esta creado con portainer+npm+mariadb.yml funcionando.
Por lo tanto se conecta a una red y un servidor DB existente, antes de levantar este dock crear las credenciales de la DB con phpmyadmin
