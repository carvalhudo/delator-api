from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.device_model import DeviceModel

class Devices(Resource):

    """Implementation of /devices endpoint"""

    def __init__(self):
        """Setup the class properties"""
        self.__req_parser = RequestParser()
        self.__req_parser.add_argument('user', type=str, required=True)
        self.__req_parser.add_argument('pass', type=str, required=True)

    def get(self):
        """
        GET /devices implementation

        :returns: The data of all registered devices or the suitable error message.
        """
        try:
            args = self.__req_parser.parse_args()

            data = DeviceModel(args['user'], args['pass']).get_all()
            if data:
                return data, 200

            return {'message': 'no devices registered!'}, 404
        except:
            return {'message': 'internal server error!'}, 500
