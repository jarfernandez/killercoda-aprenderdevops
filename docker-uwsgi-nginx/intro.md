
<br>

Vamos a desplegar una aplicación web desarrollada en Python con el framework Flask que se ejecuta en dos 
contenedores Docker con el servidor uWSGI. Se utiliza un servidor NGINX, también en un contenedor Docker, 
como proxy inverso y balanceador de carga entre ambos servidores uWSGI.