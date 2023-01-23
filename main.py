from bottle import route, run
from sum import sum


@route("/")
def index():
    return "Hello World !"


@route("/add/<a>/<b>")
def add(a, b):
    return {"result": sum(a, b)}


run(host="localhost", port=8080)
