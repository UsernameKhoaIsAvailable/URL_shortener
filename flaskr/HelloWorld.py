from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello_world.html')


@app.route('/page')
def hello_world_in_page():
    return render_template('hello_world_in_page.html')
