from flask_restful import Resource
from flask_restful.reqparse import RequestParser

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
        try:
            args = self.__req_parser.parse_args()

            data = DeviceModel(args['user'], args['pass']).get(device_id)
            if data:
                return data, 200

            return {'message': 'device not registered!'}, 404
        except:
            return {'message': 'internal server error!'}, 500

    def post(self, device_id):
        """
        POST /device/<id> implementation

        :device_id: The ID of device
        :returns: A success message if the device was registered on database; otherwise
                  the suitable error message

        """
        try:
            self.__req_parser.add_argument('serial-number', type=str, required=True)
            self.__req_parser.add_argument('description', type=str, required=True)
            self.__req_parser.add_argument('group', type=str, required=True)

            args = self.__req_parser.parse_args()
            model = DeviceModel(args['user'], args['pass'])

            if not model.get(device_id):
                model.insert(device_id, args['serial-number'], args['description'], args['group'])
                return {'message': 'device registered!'}, 201

            return {'message': 'the device is already registered!'}, 409
        except:
            return {'message': 'internal server error!'}, 500
