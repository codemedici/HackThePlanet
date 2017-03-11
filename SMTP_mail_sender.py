#!/usr/bin/env python3

import smtplib
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
SMTP_SERVER = 'aspmx.l.google.com'
SMTP_PORT = 25
 
def send_email(sender, recipient):
    """ Send email message """
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['From'] = sender
    subject = input('Enter your email subject: ')
    msg['Subject'] = subject
    message = input('Enter your email message. Press Enter when finished. ')
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)
    # create smtp session
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.set_debuglevel(1)
    session.ehlo()
    # send mail
    session.sendmail(sender, recipient, msg.as_string())
    print("You email is sent to {0}.".format(recipient))
    session.quit()
 
if __name__ == '__main__':
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipeint email address: ")
    send_email(sender, recipient)

