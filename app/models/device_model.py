from os import getenv
from pymongo import MongoClient
from pymongo.errors import OperationFailure

from errors.exceptions.invalid_credentials import InvalidCredentials
from errors.exceptions.internal_server_error import InternalServerError

class DeviceModel(object):

    """Implementation of device model"""

    def __init__(self, user, passwd):
        """
        Setup the model properties

        :user: The user name
        :passwd: The user password

        """
        db_name = getenv('DB_NAME')
        db_server = getenv('DB_SERVER')

        self.__uri = 'mongodb://%s:%s@%s/%s' % (user, passwd, db_server, db_name)

    def get_all(self):
        """
        Get the properties for all registered devices

        :returns: The list of devices as well as their properties

        """
        try:
            with MongoClient(self.__uri) as client:
                collection = client.get_database()['devices']
                dev_list = [dev for dev in collection.find({}, {'_id': False})]

                return dev_list
        except OperationFailure as err:
            self.__handle_error(err.code)

    def get(self, device_id):
        """Get the data related to a given device

        :device_id: The ID of device
        :returns: The data related to device

        """
        try:
            with MongoClient(self.__uri) as client:
                collection = client.get_database()['devices']
                dev = collection.find_one({'id': device_id}, {'_id': False})

                return dev
        except OperationFailure as err:
            self.__handle_error(err.code)

    def insert(self, device_id, serial_number, description, group):
        """
        Insert a new device into database

        :device_id: The ID of device
        :serial_number: Serial number of device
        :description: The description of the device
        :group: The group of device

        """
        try:
            with MongoClient(self.__uri) as client:
                client.get_database()['devices'].insert_one(
                    {
                        'id': device_id,
                        'serial-number': serial_number,
                        'description': description,
                        'status': 'offline',
                        'group': group,
                        'coordinates': ''
                    }
                )
        except OperationFailure as err:
            self.__handle_error(err.code)

    def remove(self, device_id):
        """
        Remove a device from database

        :device_id: The ID of device

        """
        try:
            with MongoClient(self.__uri) as client:
                client.get_database()['devices'].remove({'id': device_id})
        except OperationFailure as err:
            self.__handle_error(err.code)

    def update(self, device_id, param, value):
        """
        Update a device on database

        :device_id: The ID of device
        :param: Name of parameter to be updated
        :value: The new value for the specified parameter

        """
        try:
            with MongoClient(self.__uri) as client:
                client.get_database()['devices'].update_one(
                    {'id': device_id},
                    {'$set': {param: value}}
                )
        except OperationFailure as err:
            self.__handle_error(err.code)

    def __handle_error(self, code):
        """
        Handle an error ocurred during model handling

        :code: Code of the error

        """
        if code == 18:
            raise InvalidCredentials

        raise InternalServerError
