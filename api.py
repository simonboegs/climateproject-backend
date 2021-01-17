from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import main

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'whatup': 'dawg'}

api.add_resource(Test,'/test/')

if __name__ == '__main__':
    app.run(debug=True)
