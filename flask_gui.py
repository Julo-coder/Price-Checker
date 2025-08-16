from flask import Flask, render_template

from flaskwebgui import FlaskUI

app = Flask(__name__)

ui = FlaskUI(app=app, server='flask' ,width=500, height=500)

@app.route('/')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run()
    ui.run()