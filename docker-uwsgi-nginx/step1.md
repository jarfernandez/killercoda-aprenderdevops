
<br>

Vamos a utilizar una aplicación web Python desarrollada con Flask muy sencilla.

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