from flask import Flask
from flask_restful import Resource, Api

from resources.device import Device
from resources.devices import Devices

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Devices, '/devices')
    api.add_resource(Device, '/device/<string:device_id>')

    app.run(host='0.0.0.0', port=5000, debug=True)
