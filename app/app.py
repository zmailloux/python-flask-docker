from flask import Flask,render_template
from pymongo import MongoClient
import os
import socket

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost:27017')

print(f"Mongo Host: {MONGO_HOST}")

app = Flask(__name__)

myclient = MongoClient(MONGO_HOST)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


@app.route("/test/<text>", methods=['GET'])
def page_one(text):
    try:
        return render_template('test.html', text=text)
    except:
        return render_template('error.html')


@app.route("/add/<name>", methods=['GET'])
def add_name(name):
    namescol = myclient["flaskapp"]["names"]
    x = namescol.insert({"name": name})
    print(x)
    return render_template('added.html', text=name)

@app.route("/get", methods=['GET'])
def get_names():
    try:
        print("hey")
        flaskdb = myclient["flaskapp"]
        namescol = flaskdb["names"]
        names = namescol.find({})
        print(names)
        print([x for x in names])
        return render_template('get.html', text=[x for x in names])
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
