#!/usr/bin/env python

import paramiko
import getpass

# Open a transport
hostname = 's2lab.isg.rhul.ac.uk'
port = 40021
ssh_transport = paramiko.Transport((hostname, port))

# Auth
username = raw_input("Enter username: ")
password = getpass.getpass(prompt="Enter password: ")
ssh_transport.connect(username=username, password=password)

# Go!
sftp_session = paramiko.SFTPClient.from_transport(ssh_transport)

# Download
file_path = '/home/whoami/whoami-solutions.tar.gz' # The file to download (full path)
local_path = file_path.split('/')[-1] #  current directory
sftp_session.get(file_path, local_path) # paramiko's SFTP session suppports standard ftp commands such as get()

# Upload
#file_path = "~/foobar"
#local_path = "/root/foobar"
#sftp_session.put(local_path, file_path)

# Close
sftp_session.close()
ssh_transport.close()
