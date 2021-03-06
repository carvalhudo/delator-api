from logging import debug
from os import getenv

from pymongo import MongoClient
from pymongo.errors import OperationFailure

from errors.exceptions.invalid_credentials import InvalidCredentials
from errors.exceptions.internal_server_error import InternalServerError

class DbHandle(object):

    def __init__(self, user, passwd):
        """
        Setup the database connection

        :user: User name for connection
        :passwd: Password for connection

        """
        uri = 'mongodb://{}:{}@{}/{}'.format(
            user,
            passwd,
            getenv('DB_SERVER'),
            getenv('DB_NAME')
        )

        self.__client = MongoClient(uri)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__client.close()

    def get_device(self, device_id):
        """
        Get the data related to a registered device

        :device_id: The ID of device
        :returns: The data related to the requested device

        """
        try:
            collection = self.__client.get_database()['devices']
            dev = collection.find_one({'id': device_id}, {'_id': False})

            return dev
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def get_devices(self):
        """
        Get the properties for all registered devices

        :returns: The list of all registered devices

        """
        try:
            collection = self.__client.get_database()['devices']
            dev_list = [dev for dev in collection.find({}, {'_id': False})]

            return dev_list
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def insert_device(self, dev):
        """
        Insert a new device into database

        :dev: A device instance

        """
        try:
            db = self.__client.get_database()
            db['devices'].insert_one(
                {
                    'id': dev.id,
                    'serial-number': dev.serial_number,
                    'description': dev.description,
                    'status': 'offline',
                    'group': dev.group,
                    'coordinates': ''
                }
            )
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def remove_device(self, device_id):
        """
        Remove a device from database

        :device_id: The ID of device

        """
        try:
            db = self.__client.get_database()
            db['devices'].remove({'id': device_id})
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def update_device(self, device_id, param, value):
        """
        Update a device on database

        :device_id: The ID of device
        :param: Name of parameter to be updated
        :value: The new value for the specified parameter

        """
        try:
            db = self.__client.get_database()
            db['devices'].update_one(
                {'id': device_id},
                {'$set': {param: value}}
            )
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def insert_ocurrence(self, ocurrence):
        """
        Insert a new ocurrence into database

        :ocurrence: A ocurrence instance

        """
        try:
            db = self.__client.get_database()
            db['ocurrences'].insert_one(
                {
                    'device-id': ocurrence.device_id,
                    'timestamp': ocurrence.timestamp
                }
            )
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def get_ocurrences(self):
        """
        Get all the registered ocurrences

        :returns: The list of registered ocurrences

        """
        try:
            collection = self.__client.get_database()['ocurrences']
            ocurrence_list = [ocur for ocur in collection.find({}, {'_id': False})]

            return ocurrence_list
        except OperationFailure as err:
            self.__handle_error(err.code, err.details)

    def __handle_error(self, code, msg):
        """
        Handle an error ocurred during model handling

        :code: Code of the error
        :msg: The error message

        """
        debug(msg)

        if code == 18:
            raise InvalidCredentials

        raise InternalServerError
