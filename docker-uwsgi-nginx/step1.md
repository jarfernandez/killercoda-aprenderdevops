Vamos a utilizar una aplicación web muy sencilla desarrollada con Python y el framework Flask.

### webapp.py
```
from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>Hello, World!</title>
    </head>
    <body>
      <h1>Hello, World! This is {socket.gethostname()}.</h1>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
```

Vamos a ver el contenido del fichero `webapp.py`:

`cat /root/docker-uwsgi-nginx/WebApp/webapp.py`{{exec}}