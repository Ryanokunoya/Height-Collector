from flask import Flask, render_template, request

##source ./activate##

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__name__':
    app.debug = True
    app.run()
