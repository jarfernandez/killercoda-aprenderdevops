Para construir la imagen del servidor uWSGI, ejecutamos los siguientes comandos:

```
cd /root/docker-uwsgi-nginx
docker-compose build
```{{exec}}

Con el siguiente comando podemos verficar si se ha construido la imagen:

`docker images | grep uwsgi`{{exec}}

La salida de este comando debería ser algo similar a esto:

`aprenderdevops/uwsgi   latest    29f59e0c142e   10 seconds ago   948MB`