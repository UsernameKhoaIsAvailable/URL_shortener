from flask import Flask, render_template

app = Flask(__name__)


@app.route('/page')
def index():
    return render_template('hello_world_in_page.html')
