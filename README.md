# docker
Archivos de configuración para Docker Compose:

Utilidades para manejar docker con un solo servidor:

**portainer.yml - COMPROBADO**
Interfaz para manejar docker desde una web, muy completo y facil de utilizar, se configura red interna e IP estatica.

mariadb-phpmyadmin.yml
Un servidor de Base de Datos para utilizar solamente este para los demas servicios: nginx-proxy-manager, wordpress, etc. Configurado con IP estatica para conectarse con portainer.

nginx-proxy-manager-mariadb.yml
Utilitario para manejar dominios, sub-dominios, certificados, etc.

**portainer+npm+mariadb.yml - COMPROBADO**
cuatro servicios que se deben iniciar juntos para que funcionen bien: portainer + mariadb + phpmyadmin + nginx-proxy-manager.
Estan configurados con IP estatica para poder conectarse con otros docks y por nombre de host.

Utilidades para manejar via web docker swarm:

portainer-agent-stack.yml:
https://docs.portainer.io/start/install-ce/server/swarm/linux
Para manejar hasta 3 nodos con la version Community Edition o si te registras con Business Edition, para mas nodos hay que pagar.

nginx-proxy-manager.yml
https://nginxproxymanager.com/setup/
Es para manejar dominios, sub-dominios y certificados ssl

