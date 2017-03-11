import paramiko
k = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting"
c.connect( hostname = "s2lab.isg.rhul.ac.uk", username = "whoami", port=40021, pkey = k )
print "connected"
commands = [ "score", "id" ]
for command in commands:
	print "Executing {}".format( command )
	stdin , stdout, stderr = c.exec_command(command)
	print stdout.read()
	print( "Errors")
	print stderr.read()
c.close()
