from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


db = SQLAlchemy(app)
class Productkey(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   key = db.Column(db.String(100))

def __init__(self, id, key):
   self.key = id
   self.key = key

# Only uncomment this when u r running the project for the 1st time after creating database u need to comment this code
db.create_all()

class Productkeygeneration(Resource):
    def get(self):
        # Printing random id using uuid1()
        print("The random id using uuid1() is : ", end="")
        d = uuid.uuid1()
        s = str(d)
        print(type(s))
        query = Productkey(key=s)
        db.session.add(query)
        db.session.commit()
        return 200


api.add_resource(Productkeygeneration, "/productkeygeneration")

if __name__ == "__main__":
    app.run(debug=True)