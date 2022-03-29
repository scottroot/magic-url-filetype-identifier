from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from arweave_api import runArweaveAPI


app = Flask(__name__)
api = Api(app)
CORS(app)


class status (Resource):
    def get(self):
        try:
            return {'data': 'Api is Running'}
        except:
            return {'data': 'An Error Occurred during fetching Api'}


class fileurl(Resource):
    def get(self):
        response = runArweaveAPI()
        return jsonify({response})


api.add_resource(status, '/')
api.add_resource(fileurl, '/api')

if __name__ == '__main__':
    app.run(debug=True)