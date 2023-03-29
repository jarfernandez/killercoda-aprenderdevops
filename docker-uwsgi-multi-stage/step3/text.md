Para poder ejecutar nuestra aplicación web Python necesitaremos un servidor de aplicaciones WSGI como uWSGI. El fichero 
`uwsgi.ini` contiene la configuración del servidor uWSGI.

### uwsgi.ini
```
[uwsgi]
http = 0.0.0.0:$(UWSGI_HTTP_PORT)
module = $(UWSGI_APP):app
```

Vamos a ver el contenido del fichero `uwsgi.ini`:

`cat /root/docker-uwsgi-multi-stage/uwsgi.ini`{{exec}}