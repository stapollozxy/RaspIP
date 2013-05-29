###########################################################
# This is simple module allowing people to
# know the local and public ip of their raspberry pi
# Everytime the raspberry is ON and connected to a LOCAL
# and INTERNET connection an email is send to your mailbox
# with both ip addesses
###########################################################

import smtplib
import socket
import urllib2
from ConfigParser import SafeConfigParser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pdb


class RaspberryPi(object):
    """
    """
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    def __init__(self, ):
        """
        """
        self.parser = False
        self.ip_addresses = False

    def __call__(self,):
        self.initParser()
        self.getIp()
        self.sendIpAddresses()
        
    def initParser(self,):
        self.parser = SafeConfigParser()
        self.parser.read('setting.ini')

    def getOption(self, option):
        '''Return option value if exists
        '''
        return [ self.parser.get(section,option) for section in self.parser.sections() if self.parser.has_option(section, option) ][0]

    def getIp(self,):
        '''Set public and private IP addresses
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((self.getOption('local'),int(self.getOption('local_port'))))
        public_ip = urllib2.urlopen(self.getOption('public')).read() # Return public IP
        local_ip  = s.getsockname()[0] # Return local IP

        s.close()

        self.ip_addresses = local_ip,public_ip

    def sendIpAddresses(self,):
        
        username = self.getOption('username') or False
        password = self.getOption('password') or False #Maybe it should be encrypted ^_^
        recipient = self.getOption('recipient') or username
        
        SMTP_SERVER = self.getOption('server') or SMTP_SERVER
        SMTP_PORT = self.getOption('port') or SMTP_PORT
        
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
        
                                    
if __name__ == '__main__':
        pi = RaspberryPi()
        pi()