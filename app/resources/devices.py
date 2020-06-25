from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.device_model import DeviceModel
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist

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

        :returns: The data of all registered devices or the suitable error message

        """
        args = self.__req_parser.parse_args()

        data = DeviceModel(args['user'], args['pass']).get_all()
        if not data:
            raise ResourceDoesNotExist

        return data, 200
