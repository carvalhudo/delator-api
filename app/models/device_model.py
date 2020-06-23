from os import getenv
from pymongo import MongoClient

class DeviceModel(object):

    """Implementation of device model"""

    def __init__(self, user, passwd):
        """
        Setup the model properties

        :user: The user name
        :passwd: The user password

        """
        db_host = 'localhost' if getenv('VIRTUAL_ENV') else 'db'
        self.__uri = 'mongodb://%s:%s@%s/%s' % (user, passwd, db_host, getenv('DB_NAME'))

    def get_all(self):
        """
        Get the properties for all registered devices

        :returns: The list of devices as well as their properties

        """
        with MongoClient(self.__uri) as client:
            collection = client.get_database()['devices']
            dev_list = [dev for dev in collection.find({}, {'_id': False})]

            return dev_list

    def get(self, device_id):
        """Get the data related to a given device

        :device_id: The ID of device
        :returns: The data related to device

        """
        with MongoClient(self.__uri) as client:
            collection = client.get_database()['devices']
            dev = collection.find_one({'id': device_id}, {'_id': False})

            return dev

    def insert(self, device_id, serial_number, description, group):
        """
        Insert a new device into database

        :device_id: The ID of device
        :serial_number: Serial number of device
        :description: The description of the device
        :group: The group of device

        """
        with MongoClient(self.__uri) as client:
            client.get_database()['devices'].insert(
                {
                    'id': device_id,
                    'serial-number': serial_number,
                    'description': description,
                    'status': 'offline',
                    'group': group,
                    'coordinates': ''
                }
            )
