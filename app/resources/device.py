from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from errors.exceptions.resource_already_exist import ResourceAlreadyExist
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist
from models.device_model import DeviceModel

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
        args = self.__parser.parse_args()

        # request parameters
        user = args['user']
        passwd = args['pass']

        data = DeviceModel(user, passwd).get(device_id)
        if not data:
            raise ResourceDoesNotExist

        return data, 200

    def delete(self, device_id):
        """
        DELETE /device/<id> implementation

        :device_id: The ID of device
        :returns: If the requested device was deleted from database, a success
                  message with the associated code; otherwise the suitable error
                  message

        """
        args = self.__parser.parse_args()

        # request parameters
        user = args['user']
        passwd = args['pass']

        model = DeviceModel(user, passwd)
        if not model.get(device_id):
            raise ResourceDoesNotExist

        model.remove(device_id)

        return {'message': 'resource deleted!'}, 200

    def put(self, device_id):
        """
        PUT /device/<id> implementation

        :device_id: The ID of device
        :returns: If the device was updated on database, a success message with
                  the associated code; otherwise the suitable error message

        """
        self.__parser.add_argument('param', type=str, required=True)
        self.__parser.add_argument('value', type=str, required=True)

        args = self.__parser.parse_args()

        # request parameters
        user = args['user']
        passwd = args['pass']
        param = args['param']
        value = args['value']

        model = DeviceModel(user, passwd)
        if not model.get(device_id):
            raise ResourceDoesNotExist

        model.update(device_id, param, value)

        return {'message': 'resource updated!'}, 200
