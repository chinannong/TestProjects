from flask import Flask, render_template
fapp = Flask(__name__)

@fapp.route('/')
def hello_world():
   return render_template("index.html")

if __name__ == '__main__':
   fapp.run()