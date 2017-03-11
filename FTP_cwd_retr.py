#!/usr/bin/env python

import ftplib

URL = "ftp.hosteurope.de" #"ftp.kernel.org"
DIR = "mirror/ftp.kernel.org/pub/software/network/tftp/" #"/pub/software/network/tftp"
FILE = "tftp-hpa-0.11.tar.gz"

def ftp_file_download(url, USER, PASS):

    # open ftp connection
    ftp_client = ftplib.FTP(url, USER, PASS)

    # list files in the download directory
    ftp_client.cwd(DIR) # CWD change working directory
    print("File list at %s:" %url)

    files = ftp_client.dir()
    print(files)

    # download a file
    fd = open(FILE, 'wb')
    cmd = 'RETR %s' % FILE
    ftp_client.retrbinary(cmd, fd.write)
    fd.close()
    ftp_client.quit()


if __name__ == '__main__':

    ftp_file_download(url=URL, USER='anonymous', PASS='nobody@nourl.com')
