from werkzeug.exceptions import HTTPException

class InvalidCredentials(HTTPException):

    """
    Implementation of InvalidCredentials exception. This exception is raised
    when the credentials specified by user are invalid
    """

    code = 401
    description = 'The provided credentials are not valid!'
