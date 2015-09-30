from flask import Flask
app = Flask(__name__)

#front end loads a python shell i created from template folder 
#coming patch soon
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
