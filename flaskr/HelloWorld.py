import os

from flask import Flask, render_template

STATIC_DIR = os.path.abspath('/media/khoa/Download/URLShortener/flaskr/static')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('user_page.html')


@app.route('/page')
def hello_world_in_page():
    return render_template('hello_world_in_page.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
