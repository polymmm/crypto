from flask import Flask, render_template

app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

from RSA import bp as RSA_bp
app.register_blueprint(RSA_bp)