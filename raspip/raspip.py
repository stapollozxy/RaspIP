###########################################################
# This is simple module allowing people to
# know the local and public ip of their raspberry pi
# Everytime the raspberry is ON and connected to a LOCAL
# and INTERNET connection an email is send to your mailbox
# with both ip addesses
###########################################################


import socket
import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SMTP_RECIPIENTS, IP_PUBLIC_SERVER

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
       
        public_ip = requests.get(IP_PUBLIC_SERVER).content
        local_ip  = socket.gethostbyname(socket.gethostname())


        self.ip_addresses = local_ip,public_ip

    def sendIpAddresses(self,):

        try:
            username = SMTP_USERNAME or False
            password = SMTP_PASSWORD or False #Maybe it should be encrypted ^_^
            recipient = ','.join(SMTP_RECIPIENTS) or username
        
            self.SMTP_SERVER= SMTP_SERVER
            self.SMTP_PORT = SMTP_PORT
        except Exception, e:
            print(e)

        try:
            message = MIMEMultipart()
            message['From'] = username
            message['Subject'] = "RaspberryPi IP Addresses"
            message['To'] = recipient
            message['Cc'] = 'josue@josuebrunel.org'
        
            body = "Local Ip : %s | Public Ip : %s " %self.ip_addresses
            message.attach(MIMEText(body,'plain'))
        
            session =smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        
            session.ehlo()
            session.starttls()
            session.ehlo
            session.login(username, password)
        
            session.sendmail(username, recipient, message.as_string())
            session.quit()
        except Exception, e:
            print(e)
        
                                    
if __name__ == '__main__':
        pi = RaspberryPi()
        pi()
        print(pi.ip_addresses)
        