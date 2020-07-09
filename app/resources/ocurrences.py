from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist
from models.ocurrence_model import OcurrenceModel

class Ocurrences(Resource):

    """Implementation of /ocurrences endpoint"""

    def __init__(self):
        """Setup the class properties"""
        self.__parser = RequestParser()

        self.__parser.add_argument('user', type=str, required=True)
        self.__parser.add_argument('pass', type=str, required=True)

    def get(self):
        """
        GET /ocurrences implementation

        :returns: On success, the data of all registered ocurrences

        """
        args = self.__parser.parse_args()

        data = OcurrenceModel(args['user'], args['pass']).get_all()
        if not data:
            raise ResourceDoesNotExist

        return data, 200
