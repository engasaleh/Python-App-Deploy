from flask import Flask

app = Flask(__name__)

def home():
    return "Hello, Abdallah Our new DevOps Engineer!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
