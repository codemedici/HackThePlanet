"""
SNMPv2c
+++++++

Send SNMP GET request using the following options:

* with SNMPv2c, community 'public'
* over IPv4/UDP
* to an Agent at demo.snmplabs.com:161
* for two OIDs in string form

Functionally similar to:

| $ snmpget -v2c -c public demo.snmplabs.com 1.3.6.1.2.1.1.1.0 1.3.6.1.2.1.1.6.0

"""#
from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('demo.snmplabs.com', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')), # Sys description
           ObjectType(ObjectIdentity('1.3.6.1.2.1.6.13.1.3')), # TCP Local Ports
           ObjectType(ObjectIdentity('1.3.6.1.2.1.25.2.3.1.4')), # Storage Units
           ObjectType(ObjectIdentity('1.3.6.1.2.1.25.6.3.1.2')), # Software Name
           ObjectType(ObjectIdentity('1.3.6.1.2.1.25.4.2.1.2')), # Running Programs
           ObjectType(ObjectIdentity('1.3.6.1.2.1.25.4.2.1.4')), # Processes Path
           ObjectType(ObjectIdentity('1.3.6.1.4.1.77.1.2.25')), # User Accounts
           ObjectType(ObjectIdentity('1.3.6.1.2.1.25.1.6.0')), # System processes
           ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))) # Sys Location
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
