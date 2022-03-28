from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import subprocess


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
    def get(self, url):
        filetype = subprocess.check_output(['python', 'uri_request.py', url])
        filetype = filetype.decode('UTF-8').strip()
        return jsonify({'data': filetype})


api.add_resource(status, '/')
api.add_resource(fileurl, '/url/<url>')

if __name__ == '__main__':
    app.run()