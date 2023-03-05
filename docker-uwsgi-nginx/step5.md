Para facilitar la construcción de la imagen con el servidor uWSGI que contiene nuestra aplicación, y para crear, 
arrancar, parar y eliminar los contenedores que vamos a utilizar en el despliegue de la misma, utilizaremos Docker 
Compose.

### docker-compose.yml
```
version: '3.8'
 
services:
  nginx:
    image: nginx:latest
    container_name: nginx
    hostname: nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - 80:80
    restart: unless-stopped
 
  uwsgi-1:
    build: .
    image: aprenderdevops/uwsgi:latest
    container_name: uwsgi-1
    hostname: uwsgi-1
    volumes:
      - ./WebApp:/WebApp
    restart: unless-stopped
 
  uwsgi-2:
    image: aprenderdevops/uwsgi:latest
    container_name: uwsgi-2
    hostname: uwsgi-2
    volumes:
      - ./WebApp:/WebApp
    restart: unless-stopped
```

Vamos a ver el contenido del fichero `docker-compose.yml`:

`cat /root/docker-uwsgi-nginx/docker-compose.yml`{{exec}}