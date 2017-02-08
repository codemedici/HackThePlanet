#!/bin/bash

for ip in $(seq 0 254); do
ping -c1 10.2.100.$ip | grep "bytes from" |cut -d" " -f4 |cut -d":" -f1 >> ips_up.txt &
done
