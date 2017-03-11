#!/usr/bin/env python3
import getpass
import poplib

GOOGLE_POP3_SERVER = 'pop.googlemail.com'
POP3_SERVER_PORT = '995'

def fetch_email(username, password): 
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, POP3_SERVER_PORT) 
    mailbox.user(username)
    mailbox.pass_(password) 
    num_messages = len(mailbox.list()[1])
    print("Total emails: {0}".format(num_messages))
    print("Getting last message") 
    for msg in mailbox.retr(num_messages)[1]:
        print(msg)
    mailbox.quit()

if __name__ == '__main__':
    username = input("Enter your email user ID: ")
    password = getpass.getpass(prompt="Enter your email password: ") 
    fetch_email(username, password)

