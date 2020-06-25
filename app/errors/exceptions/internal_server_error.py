from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):

    """
    Implementation of InternalServerError exception. This exception is raised
    when an internal error is occurred during the request processing.
    """

    description = 'an internal error occurred during the hadling of request!'
    code = 500
