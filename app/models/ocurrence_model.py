from pymongo import MongoClient
from pymongo.errors import OperationFailure

from models.base_model import BaseModel

class OcurrenceModel(BaseModel):

    """Implementation of ocurrence model"""

    def get_all(self):
        """
        Get all the registered ocurrences

        :returns: The list of registered ocurrences

        """
        try:
            with MongoClient(self._uri) as client:
                collection = client.get_database()['ocurrences']
                ocurrence_list = [ocur for ocur in collection.find({}, {'_id': False})]

                return ocurrence_list
        except OperationFailure as err:
            self._handle_error(err.code)
