from logging import debug, info, warning

from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.db_handle import DbHandle
from models.device import Device

from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist
from errors.exceptions.resource_already_exist import ResourceAlreadyExist

class Devices(Resource):

    """Implementation of /devices endpoint"""

    def __init__(self):
        """
        Setup the request parser

        """
        self.__parser = RequestParser()

        self.__parser.add_argument('user', type=str, required=True)
        self.__parser.add_argument('pass', type=str, required=True)

    def get(self):
        """
        GET /devices implementation

        :returns: On success, the data of all registered devices; otherwise the
                  suitable error message

        """
        debug('GET /devices request received')

        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            data = db_handle.get_devices()
            if not data:
                error_msg = "there's no devices registered on database!"

                warning(error_msg)
                raise ResourceDoesNotExist(description=error_msg)

            debug(f'devices data: {data}')

            return data, 200

    def post(self):
        """
        POST /devices implementation

        :returns: If the device was successfully registered, a success message
                  with the associated code; otherwise the suitable error message

        """
        debug('POST /devices request received')

        self.__parser.add_argument('device-id', type=str, required=True)
        self.__parser.add_argument('serial-number', type=str, required=True)
        self.__parser.add_argument('description', type=str, required=True)
        self.__parser.add_argument('group', type=str, required=True)

        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            dev = Device(
                args['device-id'],
                args['serial-number'],
                args['description'],
                args['group']
            )

            if db_handle.get_device(dev.id):
                error_msg = f'the device {dev.id} already exist on database!'

                warning(error_msg)
                raise ResourceAlreadyExist(description=error_msg)

            db_handle.insert_device(dev)

            info('device registered on database!')
            debug(f'device data: {dev.__dict__}')

            return {'message': 'device registered with success!'}, 201
