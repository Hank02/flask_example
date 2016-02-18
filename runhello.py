from flask import Flask, render_template
from datetime import datetime
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('template.html', current_time = datetime.now(), my_name = "World", jedi_name = "")

@app.route("/<name>")
def hello(name):
    return render_template('template.html', current_time = datetime.now(), my_name = "{}".format(name.title()), jedi_name = "")

@app.route("/jedi/<name>/<last>")
def jedi(name, last):
    jname = ""
    # add first 3 letters of last name
    for i in range(3):
        jname = jname + last[i]
    # add first 2 letters of first name
    for k in range(2):
        jname = jname + name[k]
    return render_template('template.html', current_time = datetime.now(), my_name = "{}".format(name.title()), jedi_name = "{}".format(jname.title()))

@app.template_filter("formatdate")
def datetimefilter(value, format = "%Y/%m/%d %H:%M"):
    # convert a datetime stamp to a different format
    return value.strftime(format)

if __name__ == '__main__':
    #app.run(debug = True, host = "0.0.0.0", port = 8080)
    app.run(debug = True, host = environ['IP'], port = int(environ['PORT']))