from os import getenv

from errors.exceptions.invalid_credentials import InvalidCredentials
from errors.exceptions.internal_server_error import InternalServerError

class BaseModel(object):

    """Base class for models"""

    def __init__(self, user, passwd):
        """
        Setup the database uri

        :user: The user name
        :passwd: The user password

        """
        db_name = getenv('DB_NAME')
        db_server = getenv('DB_SERVER')

        self._uri = f'mongodb://{user}:{passwd}@{db_server}/{db_name}'

    def _handle_error(self, code):
        """
        Handle an error ocurred during model handling

        :code: Code of the error

        """
        if code == 18:
            raise InvalidCredentials

        raise InternalServerError
