from flask import Flask
from flask_restful import Resource, Api

from errors.errors import errors_dict
from resources.device import Device
from resources.devices import Devices

app = Flask(__name__)
api = Api(app, errors=errors_dict)

api.add_resource(Devices, '/devices')
api.add_resource(Device, '/device/<string:device_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
