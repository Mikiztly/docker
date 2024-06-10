# docker
Archivos de configuración para Docker Compose, en el directorio compose estan los ejemplos para utilizar con un solo nodo. En el directorio swarm estan los archivos configurados con un swarm de 3 workers, es la configuracion que voy a utilizar para hacer las pruebas

Utilidades para manejar docker con un solo servidor:

**portainer.yml - COMPROBADO**

Se puede utilizar en la consola: <br>
wget -O docker-compose.yml https://github.com/Mikiztly/docker/raw/main/compose/portainer.yml

https://docs.portainer.io/start/install-ce/server/swarm/linux
Para manejar hasta 3 nodos con la version Community Edition o si te registras con Business Edition, para mas nodos hay que pagar, es una interfaz para manejar docker desde una web muy completa y facil de utilizar. Es la configuracion basica para ver si nos convence, si se va a utilizar para produccion se deben hacer muchos cambios.

**portainer+npm+mariadb.yml - COMPROBADO**

Se puede utilizar en la consola:<br>
wget -O docker-compose.yml https://github.com/Mikiztly/docker/raw/main/compose/portainer+npm+mariadb.yml

Cuatro servicios que se deben iniciar juntos para que funcionen bien: portainer + mariadb + phpmyadmin + nginx-proxy-manager. Estan configurados con IP estatica para poder conectarse con otros docks y por nombre de host, hay que tener cuidado con dos aspectos muy importantes:<br>
    1) la declaracion de IP es estatica para poder incorporar mas servicios, para agregar un nuevo servicio se debe declarar la IP y configurar la lan como "external: true"<br>
    2) Los puertos no se declaran ya que se manejan con el NPM (Nginx-Proxy-Manager)

Nginx-Proxy-Manager<br>
https://nginxproxymanager.com/setup/<br>
Segun la documentacion oficial sirve para proporcionar a los usuarios una manera fácil de configurar hosts con un proxy inverso y certificados SSL, tiene que ser tan fácil que un mono puede hacerlo. En resumen sirve para manejar dominios, sub-dominios y certificados ssl, etc.

**wordpress-mariadb.yml - COMPROBADO**

Popular motor de creacion de paginas web muy flexible y configurable, esta creado con portainer+npm+mariadb.yml funcionando.
Por lo tanto se conecta a una red y un servidor DB existente, antes de levantar este dock crear las credenciales con phpmyadmin
