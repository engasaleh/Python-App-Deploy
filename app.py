from flask import Flask

app = Flask(__name__)

def home():
    return "<h1>Hello, OpenShift!</h1><h2>Hello, Abdallah Our new DevOps Engineer!</h2>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
