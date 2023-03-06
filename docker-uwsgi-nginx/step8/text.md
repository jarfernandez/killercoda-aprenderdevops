Para arrancar los servidores uWSGI y el servidor NGINX, ejecutamos el siguiente comando:

`docker-compose up -d`{{exec}}

Para verificar que todos los contenedores están arrancados, ejecutamos el siguiente comando:

`docker-compose ps`{{exec}}

Podemos ver los logs de los contenedores con el siguiente comando:

`docker-compose logs`{{exec}}

Para comprobar que la aplicación está funcionando y que NGINX está balanceando las peticiones entre los dos servidores 
uWSGI podemos acceder a la aplicación en el siguiente enlace: [Acceso a la aplicación]({{TRAFFIC_HOST1_80}})

También podemos realizar la comprobación con el comando `curl`:

`curl localhost`{{exec}}

Podemos ejecutarlo varias veces para verificar que se balancean las peticiones entre los dos servidores uWSGI.