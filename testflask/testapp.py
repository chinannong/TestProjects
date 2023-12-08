from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Test!!!")
    return "Hello World!\n"

