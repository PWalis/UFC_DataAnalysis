from flask import Flask
# @app.route("/")
# def hello():
#     return "Hello World!"

def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return ("<h1>hello<h1>")
    
    return app
