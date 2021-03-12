from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello to World with Python Flask!'

app.run(host='0.0.0.0', port=8083)
