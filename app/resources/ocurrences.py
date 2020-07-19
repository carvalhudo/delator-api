from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.db_handle import DbHandle
from models.ocurrence import Ocurrence

from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist
from errors.exceptions.resource_already_exist import ResourceAlreadyExist

class Ocurrences(Resource):

    """Implementation of /ocurrences endpoint"""

    def __init__(self):
        """
        Setup the request parser

        """
        self.__parser = RequestParser()

        self.__parser.add_argument('user', type=str, required=True)
        self.__parser.add_argument('pass', type=str, required=True)

    def get(self):
        """
        GET /ocurrences implementation

        :returns: On success, the data of all registered ocurrences; otherwise
                  a suitable error message

        """
        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            data = db_handle.get_ocurrences()
            if not data:
                raise ResourceDoesNotExist

            return data, 200

    def post(self):
        """
        POST /ocurrences implementation

        :returns: If the ocurrence was successfully registered, a success message
                  with the associated code; otherwise the suitable error message

        """
        self.__parser.add_argument('device-id', type=str, required=True)
        self.__parser.add_argument('timestamp', type=str, required=True)

        args = self.__parser.parse_args()

        with DbHandle(args['user'], args['pass']) as db_handle:
            ocurrence = Ocurrence(
                args['device-id'],
                args['timestamp']
            )

            db_handle.insert_ocurrence(ocurrence)

            return {'message': 'resource created!'}, 201
