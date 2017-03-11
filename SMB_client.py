#!/usr/bin/env python

from smb.SMBConnection import SMBConnection
import tempfile

USER_ID = 'nobody'
PASSWORD = 'PASSWORD'
CLIENT = 'debian6box'
SERVER_NAME = 'COSIMODM'
IP = '10.10.10.10'
PORT = 445
SHARE = 'IPC$'
FILE_PATH ='/test.rtd'

smb_connection = SMBConnection(
        username,
        password,
        client_machine_name,
        server_name,
        use_nltm_v2 = True,
        domain = 'WORKGROUP',
        is_direct_tcp = True
        )

assert smb_connection.connect(IP, 445)

shares = smb_connection.listShares()
for share in shares;
    print share.name

files = smb_connection.listPath(share.name, '/')
for file in files:
    print file.filename

file_obj = tempfile.NamedTemporaryFile()
file_attributes, filesize = smb_connection.retrieveFile(SHARE, FILE_PATH, file_obj)

# retrieved contents are inside file_obj
file_obj.close()
