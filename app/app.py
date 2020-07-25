from logging import basicConfig as basic_config
from logging import DEBUG

from flask import Flask
from flask_restful import Resource, Api

from errors.errors import errors_dict
from resources.device import Device
from resources.devices import Devices
from resources.ocurrences import Ocurrences

def create_app():
    """
    Create a new app based on the configuration instance

    :returns: A new instance of the app

    """
    app = Flask(__name__)
    app.config.from_object('configs.' + app.config['ENV'])

    api = Api(app, errors=errors_dict)

    api.add_resource(Devices, '/devices')
    api.add_resource(Device, '/device/<string:device_id>')
    api.add_resource(Ocurrences, '/ocurrences')

    return app

if __name__ == '__main__':
    basic_config(
        level=DEBUG,
        format='%(asctime)s :: %(levelname)s :: %(message)s'
    )

    app = create_app()
    app.run()
