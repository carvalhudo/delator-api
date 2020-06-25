from werkzeug.exceptions import HTTPException

class ResourceAlreadyExist(HTTPException):

    """
    Implementation of ResourceAlreadyExist exception. This exception is raised
    when the resource to be created already exist on server.
    """

    description = 'the resource already exist!'
    code = 409
