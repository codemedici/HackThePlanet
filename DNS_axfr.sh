#!/bin/bash
# simple zone transfer bash script
# $1 is the first argument given after the bash script
# check if the argument was given otherwise print usage

if [ -z "$1" ]; then
	echo "[***] simple Zone transfer script"
	echo "[***] usage: $0 <domain name> "
	exit 0
fi

for server in $(host -t ns $1 |cut -d" " -f4);do
	host -l $1 $server |grep "has address"
done
