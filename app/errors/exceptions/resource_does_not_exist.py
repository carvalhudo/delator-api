from werkzeug.exceptions import HTTPException

class ResourceDoesNotExist(HTTPException):

    """
    Implementation of ResourceDoesNotExist exception. This exception is raised
    when the requested resource doesn't exist on server.
    """

    code = 404
    description = "The requested resource doesn't exist!"
