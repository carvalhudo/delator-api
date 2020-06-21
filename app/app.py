from flask import Flask
from flask_restful import Resource, Api

from resources.devices import Devices

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Devices, '/devices')

    app.run(host='0.0.0.0', port=5000, debug=True)
