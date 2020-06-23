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
        :returns: The data related to the device.
        """
        try:
            args = self.__req_parser.parse_args()

            data = DeviceModel(args['user'], args['pass']).get(device_id)
            if data:
                return data, 200

            return {'message': 'device not registered!'}, 200
        except:
            return {'message': 'internal server error!'}, 500
