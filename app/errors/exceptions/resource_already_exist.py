from werkzeug.exceptions import HTTPException

class ResourceAlreadyExist(HTTPException):

    """
    Implementation of ResourceAlreadyExist exception. This exception is raised
    when the resource to be created already exist on server.
    """

    code = 409
    description = 'The resource already exist!'
