for x in {1..254..1}; do ping 192.168.0.$x | grep '64 b' | cut -d" " -f4 >> ips.txt; done
