from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.device_model import DeviceModel
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist
from errors.exceptions.resource_already_exist ResourceAlreadyExist

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
        args = self.__parser.parse_args()

        # request parameters
        user = args['user']
        passwd = args['pass']

        data = DeviceModel(user, passwd).get_all()
        if not data:
            raise ResourceDoesNotExist

        return data, 200

    def post(self):
        """
        POST /devices implementation

        :returns: If the device was successfully registered, a success message
                  with the associated code; otherwise the suitable error message

        """
        self.__parser.add_argument('device-id', type=str, required=True)
        self.__parser.add_argument('serial-number', type=str, required=True)
        self.__parser.add_argument('description', type=str, required=True)
        self.__parser.add_argument('group', type=str, required=True)

        args = self.__parser.parse_args()

        # request parameters
        user = args['user']
        passwd = args['pass']
        device_id = args['device-id']
        serial_number = args['serial-number']
        description = args['description']
        group = args['group']

        model = DeviceModel(user, passwd)
        if model.get(device_id):
            raise ResourceAlreadyExist

        model.insert(device_id, serial_number, description, group)

        return {'message': 'resource created!'}, 201


