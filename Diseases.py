from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask_sslify import SSLify
import os

db_connect = create_engine('sqlite:///healthcare.db')

app = Flask(__name__)
api = Api(app)

def getApp():
    return app

class Doencas(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from doencas")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

class UserById(Resource):    

    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from doencas where id =%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

api.add_resource(Doencas, '/doencas') 
api.add_resource(UserById, '/doencas/<id>') 

#if 'DYNO' in os.environ: # only trigger SSLify if the app is running on Heroku
#    sslify = SSLify(app)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)