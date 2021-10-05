from flask import Flask
app=Flask(__name__)

@app.route("/")
def hi():
    return "Hello"

@app.route("/daz")
def names():
    return "Hello Dazz"
app.run()