Para que nuestro contenedor NGINX funcione como proxy inverso y balanceador de carga necesitamos pasarle el fichero de 
configuración `nginx.conf`.

### nginx.conf
```
user nginx;
worker_processes 1;

error_log /var/log/nginx/error.log warn;
pid       /var/run/nginx.pid;

events {
  worker_connections 1024;
}

http {
  sendfile    on;
  tcp_nopush  on;
  tcp_nodelay on;

  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Host $server_name;

  upstream uwsgi {
    server uwsgi-1:8000;
    server uwsgi-2:8000;
  }

  server {
    listen 80;

    location / {
      proxy_pass     http://uwsgi;
      proxy_redirect off;
    }
  }
}
```

Vamos a ver el contenido del fichero `nginx.conf`:

`cat /root/docker-uwsgi-nginx/nginx.conf`{{exec}}