from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())

@app.route("/hi/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src = "http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<name>/<last>")
def jedi_name(name, last):
    # variable to store Jedi name
    jedi = ""
    # add first 3 letters of last name
    for i in range(3):
        jedi = jedi + last[i]
    # add first 2 letters of first name
    for k in range(2):
        jedi = jedi + name[k]
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Your Jedi name is: {}!
        </p>
    """

    return html.format(name.title(), jedi.title())

if __name__ == "__main__":
    app.run(host = environ['IP'], port = int(environ['PORT']))