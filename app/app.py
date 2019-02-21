from flask import Flask,render_template
from pymongo import MongoClient
import os
import socket

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost:27017')

print("Trying to log into mongo...")
myclient = MongoClient(MONGO_HOST, username="admin", password="test")
print("Logged in...")

print(myclient.get_database("my-database"))


app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
