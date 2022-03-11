from flask import Flask

app: Flask = Flask(__name__)


@app.route("/greeting", methods=["GET"])
def hello_world():
    return "Hello world!"


@app.route("/personal/<name>", methods=["GET"])
def personal_greeting(name: str):
    return f"hello {name}!"


app.run()
