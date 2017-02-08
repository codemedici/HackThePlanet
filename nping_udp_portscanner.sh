#!/bin/bash

for ip in $(seq 0 254); do
ping -c1 192.168.0.$ip | grep "bytes from" |cut -d" " -f4 |cut -d":" -f1 >> ping.txt &
done

for ip in $(cat ping.txt);
do
        for port in $(seq 1 2048);
        do
                nping --udp -p $port $ip -c 1 >> ip_udp_recv.txt &
        done
done

grep "RECV" ip_udp_recv.txt | cut -d" " -f9 | sort -u
