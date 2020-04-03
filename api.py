from flask import Flask
#from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

@app.route("/")
def dummy_api():
    return "Darshan's first API"

@app.route("/check_routes/<name>")
def dynamic(name):
    return "This is dynamic page with %s !" % name

@app.route("/check_routes")
def check_routes():
    return "Darshan is checking routes"

if __name__ == "__main__":
    app.run(debug=True)