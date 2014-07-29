###########################################################
# This is simple module allowing people to
# know the local and public ip of their raspberry pi
# Everytime the raspberry is ON and connected to a LOCAL
# and INTERNET connection an email is send to your mailbox
# with both ip addesses
###########################################################


import socket
import requests

import mail
from config import IP_PUBLIC_SERVER

import pdb

class RaspberryPi(object):
    """
    """

    def __init__(self, ):
        """
        """
        self.parser = False
        self.ip_addresses = False

    def __call__(self,):
        self.getIp()
        self.sendIpAddresses()

    def getIp(self,):
        '''Set public and private IP addresses
        '''
        try:
            public_ip = requests.get(IP_PUBLIC_SERVER).content
        except Exception, e:
            print(e)
        finally:
            public_ip = 'No Internet Connection'
                        
        local_ip  = socket.gethostbyname(socket.gethostname())

        self.ip_addresses = local_ip,public_ip

    def sendIpAddresses(self,):
        mail.send_email(self.ip_addresses)
                                                    
if __name__ == '__main__':
        pi = RaspberryPi()
        pi()
        print(pi.ip_addresses)
        