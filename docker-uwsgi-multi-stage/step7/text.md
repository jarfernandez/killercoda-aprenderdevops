Para construir la imagen del servidor uWSGI, ejecutamos los siguientes comandos:

```
cd /root/docker-uwsgi-multi-stage
docker build -t aprenderdevops/uwsgi .
```{{exec}}

Con el siguiente comando podemos verficar si se ha construido la imagen:

`docker images | grep uwsgi`{{exec}}

La salida de este comando debería ser algo similar a esto:

`aprenderdevops/uwsgi   latest    29f59e0c142e   10 seconds ago   944MB`