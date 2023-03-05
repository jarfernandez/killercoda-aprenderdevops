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
