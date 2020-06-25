from errors.exceptions.internal_server_error import InternalServerError
from errors.exceptions.invalid_credentials import InvalidCredentials
from errors.exceptions.resource_already_exist import ResourceAlreadyExist
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist

errors_dict = {
    InvalidCredentials.name : {
        'message': InvalidCredentials.description,
        'status': InvalidCredentials.code,
    },
    ResourceDoesNotExist.name: {
        'message': ResourceDoesNotExist.description,
        'status': ResourceDoesNotExist.code,
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
