from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import main

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('latitude', type=str, required=True)
parser.add_argument('longitude', type=str, required=True)

class Test(Resource):
    def get(self):
        coordinates = {
                'latitude': parser.parse_args().get('latitude','None'),
                'longitude': parser.parse_args().get('longitude','None'),
                }
        return main.getResults(coordinates)

api.add_resource(Test,'/test/')

if __name__ == '__main__':
    app.run(debug=True)
