from flask import Flask

app = Flask(__name__)

class HelloWorld():

@app.route('/')
def index():
    return 'Hello to Participants using Python Flask!'

app.run(host='0.0.0.0', port=8082)
