Ahora vamos a construir nuevamente la imagen, pero para ello utilizaremos un `Dockerfile` multi-etapa con el siguiente 
contenido:
- Una variable de argumento `ARG PYTHON_VERSION=3.11` que se utilizará para especificar la versión de Python que se 
utilizará en el contenedor.
- Una etapa build a partir de la imagen `python` y la versión especificada en la variable de argumento anterior.
- En la etapa build se instala uWSGI y todas las librerias que necesita la aplicación.
- Una etapa run a partir de la imagen `python` y la versión especificada en la variable de argumento `PYTHON_VERSION`.
- En esta etapa es necesario volver a incluir la variable de argumento `ARG PYTHON_VERSION`.
- Variables de argumento y entorno para el puerto HTTP y la aplicación por defecto para uWSGI.
- Instalación de dependencias `RUN apt-get update && apt-get install -y libxml2`
- Creación de un usuario `admin` para arrancar uWSGI.
- Copia del contenido de la imagen builder.
- Copia del contenido de la aplicación.
- Copia del fichero con la configuración de uWSGI.
- Se establece un directorio de trabajo y un volumen con el contenido de la aplicación.
- Se inicia uWSGI con un `ENTRYPOINT`.

Se puede utilizar una plantilla del `Dockerfile` multi-etapa en `/root/docker-uwsgi-multi-stage/Dockerfile-multi-stage`.

<details><summary>Pista</summary><p>
# Version de Python (solo mayor y menor)
ARG PYTHON_VERSION=3.11

# Etapa build
FROM python:${PYTHON_VERSION} AS build

# Se instala uWSGI y todas las librerias que necesita la aplicacion
COPY WebApp/requirements.txt requirements.txt
RUN pip install uwsgi && pip install -r requirements.txt

# Etapa run
FROM python:${PYTHON_VERSION}-slim AS run

# Es necesario volver a incluir en esta etapa esta variable
ARG PYTHON_VERSION

# Puerto HTTP por defecto para uWSGI
ARG UWSGI_HTTP_PORT=8000
ENV UWSGI_HTTP_PORT=$UWSGI_HTTP_PORT

# Aplicacion por defecto para uWSGI
ARG UWSGI_APP=webapp
ENV UWSGI_APP=$UWSGI_APP

# Se instalan dependencias
RUN apt-get update && apt-get install -y libxml2

# Se crea un usuario para arrancar uWSGI
RUN useradd -ms /bin/bash admin
USER admin

# Se copia el contenido de la imagen builder
COPY --from=build /usr/local/lib/python${PYTHON_VERSION}/site-packages /usr/local/lib/python${PYTHON_VERSION}/site-packages
COPY --from=build /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# Se copia el contenido de la aplicacion
COPY WebApp /WebApp

# Se copia el fichero con la configuración de uWSGI
COPY uwsgi.ini uwsgi.ini

# Se establece el directorio de trabajo
WORKDIR /WebApp

# Se crea un volumen con el contenido de la aplicacion
VOLUME /WebApp

# Se inicia uWSGI
ENTRYPOINT ["uwsgi", "--ini", "/uwsgi.ini"]
</p></details>