import raspip
import unittest

from raspip import RaspberryPi

class RaspIpTestCase(unittest.TestCase):

    def setUp(self,):
        self.pi = raspip.RaspberryPi()

    def tearDown(self):
        pass

    def testHostname(self,):
        self.assertEquals('LokingMac.local', self.pi.getHostname())

class RaspIP_TestHostname():
    def test_hostname(self,):
        self.testHostname()


if __name__ == '__main__':
    unittest.main()