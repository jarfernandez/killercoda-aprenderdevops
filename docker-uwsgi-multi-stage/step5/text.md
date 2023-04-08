Para construir la imagen del servidor uWSGI, ejecutamos los siguientes comandos:

```
cd /root/docker-uwsgi-multi-stage
docker build -t aprenderdevops/uwsgi:1.0.0 .
```{{exec}}

Con el siguiente comando podemos verficar si se ha construido la imagen:

`docker images | grep uwsgi`{{exec}}

La salida de este comando debería ser algo similar a esto:

`aprenderdevops/uwsgi   1.0.0     000bd833d12a   2 minutes ago   944MB`

> La imagen tiene un tamaño de más de 900MB.