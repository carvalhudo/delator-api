from exceptions.internal_server_error import InternalServerError
from exceptions.invalid_credentials import InvalidCredentials
from exceptions.resource_does_not_exist import ResourceDoesNotExist
from exceptions.resource_already_exist import ResourceAlreadyExist

errors_dict = {
    InvalidCredentials.name : {
        'message': InvalidCredentials.description,
        'status': InvalidCredentials.code,
    },
    ResourceAlreadyExist.name: {
        'message': ResourceDoesNotExist.description,
        'status': ResourceAlreadyExist.code,
    },
    ResourceAlreadyExist.name: {
        'message': ResourceAlreadyExist.description,
        'status': ResourceAlreadyExist.code,
    },
    InternalServerError.name: {
        'message': InternalServerError.description,
        'status': InternalServerError.code,
    }
}
