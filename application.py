from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print('hello method invoked')
    return "Hello Azure! from Python.  Let's see what you can do."
