from os import getenv
from pymongo import MongoClient

class DeviceModel(object):

    """Implementation of device model"""

    def __init__(self, user, passwd):
        """Setup the model properties

        :user: The user name.
        :passwd: The user password.
        """
        db_host = 'localhost' if getenv('VIRTUAL_ENV') else 'db'
        self.__uri = 'mongodb://%s:%s@%s/%s' % (user, passwd, db_host, getenv('DB_NAME'))

    def get_all(self):
        """
        Get the properties for all registered devices.

        :returns: The list of devices as well as their properties.
        """
        with MongoClient(self.__uri) as client:
            collection = client.get_database()['devices']
            dev_list = [dev for dev in collection.find({}, {'_id': False})]

            return dev_list
