from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def hi():
    return render_template('index.html')

@app.route("/daz")
def names():
    return "Hello Dazz"
app.run()