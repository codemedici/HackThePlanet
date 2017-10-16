#!/usr/bin/python
import socket
import sys
import re
import os

if len(sys.argv) != 3:
    print "usage smtp_verify_userlist.py <ip> <userlist.txt>"
    sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
f = open(sys.argv[2], 'r')

s.connect((str(sys.argv[1]), 25))
print s.recv(1024)

s.send('EHLO world\r\n')
print s.recv(1024)

for line in f.readlines():
    # change EXPN for VRFY or viceversa
    s.send('EXPN ' + line + '\r\n')
    result = s.recv(1024)
    if re.search('250',result):
        print result

s.close()
