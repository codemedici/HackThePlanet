import os

for host in range(200,254):
    ip = '192.168.33.'+str(host)
    response = os.system('ping -c 1 '+ ip)
    if response == 0:
        print ip + ' UP'
    else:
        print ip + ' DOWN'
