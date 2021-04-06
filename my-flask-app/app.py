from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/user/<name>')
def user(name):
    return render_template('hello.html', name=name)
