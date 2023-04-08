Para construir la imagen del servidor uWSGI con construcción multi-etapa, ejecutamos los siguientes comandos:

```
cd /root/docker-uwsgi-multi-stage
docker build -f Dockerfile-multi-stage -t aprenderdevops/uwsgi:2.0.0 .
```{{exec}}

Con el siguiente comando podemos verficar si se ha construido la imagen:

`docker images | grep uwsgi`{{exec}}

La salida de este comando debería ser algo similar a esto:

```
aprenderdevops/uwsgi   2.0.0       7c9601a743f9   25 seconds ago   209MB
aprenderdevops/uwsgi   1.0.0       000bd833d12a   6 minutes ago    944MB
```

> La nueva imagen tiene un tamaño inferior a la anterior.