from pysnmp.hlapi import *

'''
+++ similar to 'onesixtyone -c communityfile.txt -i hosts.txt'
+++ allows more than 32 community string (default max in -c option of onesixyone)
+++ allows to specify multiple MIB values
+++ similar to snmpget -v2c -c public demo.snmplabs.com 1.3.6.1.2.1.1.1.0  ... ...
--- needs multithreading to deal with udp response times, otherwise too slow!
'''

# read ips from a text file
with open('ips.txt', 'r') as f:
    ips = f.read().splitlines()

# read community strings from a text file
# https://github.com/danielmiessler/SecLists/blob/master/Miscellaneous/wordlist-common-snmp-community-strings.txt
with open('wordlist-common-snmp-community-strings.txt', 'r') as f:
    community = f.read().splitlines()


for ip in ips:

    #for string in community:

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
            CommunityData('public'), # community str
            UdpTransportTarget((ip, 161)), # ip
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)), # sys description
            ObjectType(ObjectIdentity('1.3.6.1.2.1.6.13.1.3')), # TCP Local Ports
            ObjectType(ObjectIdentity('1.3.6.1.2.1.25.2.3.1.4')), # Storage Units
            ObjectType(ObjectIdentity('1.3.6.1.2.1.25.6.3.1.2')), # Software Name
            ObjectType(ObjectIdentity('1.3.6.1.2.1.25.4.2.1.2')), # Running Programs
            ObjectType(ObjectIdentity('1.3.6.1.2.1.25.4.2.1.4')), # Processes Path
            ObjectType(ObjectIdentity('1.3.6.1.4.1.77.1.2.25')), # User Accounts
            ObjectType(ObjectIdentity('1.3.6.1.2.1.25.1.6.0')), # System processes
            ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')) # Sys Location
 )
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
