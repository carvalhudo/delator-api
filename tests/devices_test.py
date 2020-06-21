import unittest
import unittest.mock

class DeviceEndpointTest(unittest.TestCase):

    """Implementation of unit tests for /devices endpoint"""

    def setUp(self):
        """"""

    def tearDown(self):
        """"""

    def multiple_devices_registered_test(self):
        """
        GIVEN the device model contains multiple devices registered.
        WHEN  the client performs a GET operation on /devices endpoint.
        THEN  the API must return the data of all registered devices.
        """

    def one_device_registered_test(self):
        """
        GIVEN the device model contains just one device registered.
        WHEN  the client performs a GET operation on /devices endpoint.
        THEN  the API must return the data of the single registered device.
        """

    def no_device_registered_test(self):
        """
        GIVEN the device model is empty.
        WHEN  the client performs a GET operation on /devices endpoint.
        THEN  the API must return an error message.
        """

if __name__ == "__main__":
    unittest.main()
