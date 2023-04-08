Para arrancar la aplicación, ejecutamos el siguiente comando:

`docker run -d -p 8080:8000 --restart unless-stopped -v $(pwd)/WebApp:/WebApp aprenderdevops/uwsgi:2.0.0`{{exec}}

Para verificar que el contenedor está arrancado, ejecutamos el siguiente comando:

`docker ps`{{exec}}

Para comprobar que la aplicación está funcionando podemos acceder a la aplicación en el siguiente enlace: 
[Acceso a la aplicación]({{TRAFFIC_HOST1_8080}})

También podemos realizar la comprobación con el comando `curl`:

`curl http://localhost:8080`{{exec}}