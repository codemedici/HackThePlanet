#!/usr/bin/env python
import socket
import netifaces

if __name__ == '__main__':    
    # Find host info
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: {0}".format(host_name))
    
    # Get interfaces list
    ifaces = netifaces.interfaces()
    for iface in ifaces:
        ipaddrs = netifaces.ifaddresses(iface)
        if ipaddrs.has_key(netifaces.AF_INET):
            ipaddr_desc = ipaddrs[netifaces.AF_INET]
            ipaddr_desc = ipaddr_desc[0]
            print("Network interface: {0}".format(iface))
            print("\tIP address: {0}".format(ipaddr_desc['addr']))
            print("\tNetmask: {0}".format(ipaddr_desc['netmask']))
    # Find the gateway
    gateways = netifaces.gateways()
    print("Default gateway: {0}".format(gateways['default'][netifaces.AF_INET][0]))

    
