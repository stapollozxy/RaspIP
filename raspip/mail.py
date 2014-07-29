import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from threading import Thread

from config import SMTP_USERNAME, SMTP_PASSWORD, SMTP_RECIPIENTS, SMTP_SERVER, SMTP_PORT


username = SMTP_USERNAME or False
password = SMTP_PASSWORD or False #Maybe it should be encrypted (^_^)
recipients = ','.join(SMTP_RECIPIENTS) or username

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args= args, kwargs= kwargs)
        thr.start()
    return wrapper

@async
def send_async():
    try:
        session =smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(username, password)
        
        session.sendmail(username, recipient, message.as_string())
        session.quit()
    except Exception, e:
        print(e)


def send_email(ip_addresses):
    
    message = MIMEMultipart()
    message['From'] = username
    message['Subject'] = "RaspberryPi IP Addresses"
    message['To'] = recipients
    message['Cc'] = 'josue@josuebrunel.org'
    
    body = "Local Ip : %s | Public Ip : %s " %ip_addresses # A tuple
    message.attach(MIMEText(body,'plain'))

    
        
    
    

    