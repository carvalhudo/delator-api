from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):

    """
    Implementation of InternalServerError exception. This exception is raised
    when an internal error is occurred during the request processing.
    """

    code = 500
    description = 'An internal error occurred during the hadling of request!'
