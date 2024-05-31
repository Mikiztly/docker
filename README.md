# docker
Archivos de configuración para Docker Compose:

Utilidades para manejar docker con un solo servidor:

**portainer.yml - COMPROBADO**
Interfaz para manejar docker desde una web, muy completo y facil de utilizar, se configura red interna e IP estatica.

**mariadb-phpmyadmin.yml - COMPROBADO**
Un servidor de Base de Datos para utilizar solamente este para los demas servicios: nginx-proxy-manager, wordpress, etc. Configurado con IP estatica para conectarse con portainer.

**nginx-proxy-manager-mariadb.yml  - COMPROBADO**
Utilitario para manejar dominios, sub-dominios, certificados, etc.

Utilidades para manejar via web docker swarm:

portainer-agent-stack.yml:
https://docs.portainer.io/start/install-ce/server/swarm/linux
Para manejar hasta 3 nodos con la version Community Edition o si te registras con Business Edition, para mas nodos hay que pagar.

nginx-proxy-manager.yml
https://nginxproxymanager.com/setup/
Es para manejar dominios, sub-dominios y certificados ssl

