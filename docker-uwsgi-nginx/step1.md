Vamos a utilizar una aplicación web muy sencilla desarrollada con Python y el framework Flask.

### webapp.py
```
from flask import Flask
import socket
 
app = Flask(__name__)
 
 
@app.route("/")
def hello():
    return f"Hello World from {socket.gethostname()}!"
 
 
if __name__ == "__main__":
    app.run()
```