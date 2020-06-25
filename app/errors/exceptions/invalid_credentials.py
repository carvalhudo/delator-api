from werkzeug.exceptions import HTTPException

class InvalidCredentials(HTTPException):

    """
    Implementation of InvalidCredentials exception. This exception is raised
    when the credentials specified by user are invalid
    """

    description = 'the provided credentials are not valid!'
    code = 401
