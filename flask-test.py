from flask import Flask
from os import environ

prog = Flask(__name__)

@prog.route("/<name>")
def func1(name):
    html = """
    <h1>Hello {}, welcome!</h1>
    <p>Quick Flask test.</p>
    <h3>Good bye {}!</h3>
    """
    return html.format(name.title(), name.title())

if __name__ == "__main__":
    prog.run(host = environ['IP'], port = int(environ['PORT']))