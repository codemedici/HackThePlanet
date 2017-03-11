#!/usr/bin/env python

import paramiko
import getpass

HOSTNAME = 's2lab.isg.rhul.ac.uk'
PORT = 40021

def connect(username, password, hostname=HOSTNAME, port=PORT):

    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.load_system_host_keys()

    c.connect(hostname, port, username, password)
    return c


def run_ssh_cmd(c):

    cmd = ""

    while cmd != "exit":
        cmd = raw_input("cmd > ")
        stdin, stdout, stderr = c.exec_command(cmd)
        print(stdout.read())
        print(stderr.read())

    c.close()


if __name__=='__main__':

    username = raw_input("Enter username: ")
    password = getpass.getpass(prompt="Enter password: ")

    ssh_client = connect(username, password)

    run_ssh_cmd(ssh_client)
