
class Ocurrence(object):

    """Model for ocurrence"""

    def __init__(self, device_id, timestamp):
        """
        Setup the ocurrence properties

        :device_id: ID of device
        :timestamp: Timestamp of ocurrence

        """
        self.device_id = device_id
        self.timestamp = timestamp
