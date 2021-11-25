import unittest
import socialCoding

class TestClass(unittest.TestCase):

    def test_success(self):
        ipAdd = input("Input IP Address: ")
        self.assertTrue(socialCoding.IpGeoLocation.check(ipAdd))

if __name__ == '__main__':
    unittest.main()