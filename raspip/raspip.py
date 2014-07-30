###########################################################
# This is simple module allowing people to
# know the local and public ip of their raspberry pi
# Everytime the raspberry is ON and connected to a LOCAL
# and INTERNET connection an email is send to your mailbox
# with both ip addesses
###########################################################

import socket
import requests
from sys import platform

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

    def getHostLocalAddress(self,):
        
        if platform == "darwin":
            hostname = socket.gethostname() if '.local' in socket.gethostname() else socket.gethostname()+'.local' #OS X where hostname doesn't have the <.local>
            return socket.gethostbyname(hostname)
        else:
            return socket.gethostbyname(socket.gethostname())

    def getIp(self,):
        '''Set public and private IP addresses
        '''
        try:
            public_ip = requests.get(IP_PUBLIC_SERVER).content
        except Exception, e:
            print(e)
            public_ip = 'None : no internet connection'
        #finally:
            
        local_ip  = self.getHostLocalAddress()
       
        self.ip_addresses = local_ip,public_ip

    def sendIpAddresses(self,):
        mail.send_email(self.ip_addresses)
                                                    
# if __name__ == '__main__':
#     pi = RaspberryPi()
#     pi()
#     print(pi.ip_addresses)
        