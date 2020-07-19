
class Device(object):

    """Model for Device"""

    def __init__(self, device_id, serial_number, description, group):
        """
        Setup the device properties

        :device_id: Id of device
        :serial_number: Serial number of device
        :description: Description of device
        :group: Group of device

        """
        self.device_id = device_id
        self.serial_number = serial_number
        self.description = description
        self.group = group