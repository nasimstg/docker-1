from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello, This is a flask app running inside a docker container!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)