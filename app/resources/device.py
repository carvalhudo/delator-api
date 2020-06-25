from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from errors.exceptions.resource_already_exist import ResourceAlreadyExist
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist
from models.device_model import DeviceModel

class Device(Resource):

    """Implementation of /device/<id> endpoint"""

    def __init__(self):
        """Setup the class properties"""
        self.__req_parser = RequestParser()
        self.__req_parser.add_argument('user', type=str, required=True)
        self.__req_parser.add_argument('pass', type=str, required=True)

    def get(self, device_id):
        """
        GET /device/<id> implementation

        :device_id: The ID of device
        :returns: The data related to the device or the suitable error message

        """
        args = self.__req_parser.parse_args()

        data = DeviceModel(args['user'], args['pass']).get(device_id)
        if not data:
            raise ResourceDoesNotExist

        return data, 200

    def post(self, device_id):
        """
        POST /device/<id> implementation

        :device_id: The ID of device
        :returns: A success message if the device was registered on database; otherwise
                  the suitable error message

        """
        self.__req_parser.add_argument('serial-number', type=str, required=True)
        self.__req_parser.add_argument('description', type=str, required=True)
        self.__req_parser.add_argument('group', type=str, required=True)

        args = self.__req_parser.parse_args()

        model = DeviceModel(args['user'], args['pass'])
        if model.get(device_id):
            raise ResourceAlreadyExist

        model.insert(device_id, args['serial-number'], args['description'], args['group'])

        return {'message': 'resource created!'}, 201

    def delete(self, device_id):
        """
        DELETE /device/<id> implementation

        :device_id: The ID of device
        :returns: A success message if the device was deleted properly; otherwise the suitable
                  error message

        """
        args = self.__req_parser.parse_args()

        model = DeviceModel(args['user'], args['pass'])
        if not model.get(device_id):
            raise ResourceDoesNotExist

        model.remove(device_id)

        return {'message': 'resource deleted!'}, 200

    def put(self, device_id):
        """
        PUT /device/<id> implementation

        :device_id: The ID of device
        :returns: A success message if the device was updated on database; otherwise the suitable
                  error message

        """
        # TODO: fix the case where the client specifies a parameter who doesn't exist on document

        self.__req_parser.add_argument('param', type=str, required=True)
        self.__req_parser.add_argument('value', type=str, required=True)

        args = self.__req_parser.parse_args()

        model = DeviceModel(args['user'], args['pass'])
        if not model.get(device_id):
            raise ResourceDoesNotExist

        model.update(device_id, args['param'], args['value'])

        return {'message': 'resource updated!'}, 200
