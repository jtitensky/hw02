from flask import Flask
app=Flask(__name__)

@app.route("/")
def zero():
    return "page 0"

@app.route("/1")
def one():
    return "page 1"

@app.route("/2")
def two():
    return "page2"

if __name__=="__main__":
    app.run()
