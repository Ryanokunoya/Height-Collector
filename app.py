import logging
import sys

import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from send_email import send_email

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://edxbuzcmhlvutv:e4ceb0c18ec64e1744db1ebcd0143a73bb00e85fc613e1aa2a048c537ffac832@ec2-34-192-122-0.compute-1.amazonaws.com:5432/d7bsc0jsrbp15c?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = round(db.session.query(
                func.avg(Data.height_)).scalar(), 1)
            count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template('index.html', text="This email is already used with another height")


if __name__ == '__main__':
    app.debug = True
    app.run()
