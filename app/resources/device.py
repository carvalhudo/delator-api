from logging import debug, info, warning

from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.db_handle import DbHandle

from errors.exceptions.resource_already_exist import ResourceAlreadyExist
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist

class Device(Resource):

    """Implementation of /device/<id> endpoint"""

    def __init__(self):
        """
        Setup the request parser

        """
        self.__parser = RequestParser()

        self.__parser.add_argument('user', type=str, required=True)
        self.__parser.add_argument('pass', type=str, required=True)

    def get(self, device_id):
        """
        GET /device/<id> implementation

        :device_id: The ID of device
        :returns: If the device exist on database, the data related to the
                  requested device; otherwise the suitable error message

        """
        debug('GET /device/<id> request received')

        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            data = db_handle.get_device(device_id)
            if not data:
                error_msg = f"the device {device_id} isn't registered on database!"

                warning(error_msg)
                raise ResourceDoesNotExist(description=error_msg)

            debug(f'device data: {data}')

            return data, 200

    def delete(self, device_id):
        """
        DELETE /device/<id> implementation

        :device_id: The ID of device
        :returns: If the requested device was successfully deleted from
                  database, a success message with the associated code;
                  otherwise the suitable error message

        """
        debug('DELETE /device/<id> request received')

        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            if not db_handle.get_device(device_id):
                error_msg = f"the device {device_id} isn't registered on database!"

                warning(error_msg)
                raise ResourceDoesNotExist(description=error_msg)

            db_handle.remove_device(device_id)

            info(f'device {device_id} was removed from database!')

            return {'message': 'device unregistered with success!'}, 200

    def put(self, device_id):
        """
        PUT /device/<id> implementation

        :device_id: The ID of device
        :returns: If the device was successfully updated on database, a
                  success message with the associated code; otherwise the
                  suitable error message

        """
        debug('PUT /device/<id> request received')

        self.__parser.add_argument('param', type=str, required=True)
        self.__parser.add_argument('value', type=str, required=True)

        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            if not db_handle.get_device(device_id):
                error_msg = f"the device {device_id} isn't registered on database!"

                warning(error_msg)
                raise ResourceDoesNotExist(description=error_msg)

            db_handle.update_device(
                device_id,
                args['param'],
                args['value']
            )

            info(f'device {device_id} was updated on database!')
            debug("new value for '{}': '{}'".format(
                args['param'],
                args['value']
            ))

            return {'message': 'device updated with success!'}, 200
