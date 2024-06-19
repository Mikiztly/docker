En esta carpeta estan por separados los servidores y exportadores para poder levantarlos segun lo que haga falta, tambien estan los archivos de configuracion para prometheus que permiten agregar sitios y maquinas a monitorizar sin tener que reiniciar el servidor prometheus:

**grafana.yml**

Motor para crear graficos y dashboards desde distintos servicios, prometheus, loki, zabbix, etc.
Se delaro una URL personalizada para mejor acceso
Tiene instalados 2 plugins:<br>
1) grafana-clock-panel -> Un reloj bastante configurable
2) alexanderzobnin-zabbix-app -> Sirve para conectarse a un Zabbix y poder graficar con esos datos

**IMPORTANTE**
Hay que crear la carpeta:
* /grafana-data -> en esta carpeta se guardan los datos de grafana

**prometheus.yml**

Base de datos para utilizar con grafana, sirve para recolectar datos de varias fuentes, hay que generar las carpetas y subir el archivo prometheus-config.yml para que funcione bien el servidor.

**IMPORTANTE**
Hay que crear dos carpetas:
* /prometheus/config -> en esta carpeta vamos a cargar los archivos de configuracion de prometheus
* /prometheus/data -> en esta carpeta se guardan los datos de prometheus

Hay tres archivos de configuracion que van en la carpeta /etc/prometheus del docker:
1) **prometheus-config.yml** esta con una configuracion personalizada con una configuracion basica para tener el monitoreo local con los 3 modulos, toma la lista de un archivo para obtener una lista de paginas web para monitorizar
2) **blackbox-targets.yml** contiene una lista de paginas que se van a monitorizar, se pueden agreagar con etiquetas como el estado y el tipo de IP utilizada para el monitoreo.
3) **nodes-targets.yml** contiene una lista de servidores que se van a monitorizar, se pueden agreagar con etiquetas

**prometheus-monitor.yml**

Stack para habilitar el monitoreo en un servidor grafana ya funcionando, tiene tres contenedores:<br>
1) node-exporter: el agente de prometheus que permite monitorizar los recursos de linux. Dashboard de testeo: 11074
2) blackbox-exporter: el agente para monitorizar paginas web. Dashboard de testeo: 13659
3) cadvisor: un agente de codigo libre perteneciente a google que sirve para monitorizar contenedores. Dashboard de testeo: 193
