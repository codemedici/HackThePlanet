#!/usr/bin/env python
from itertools import permutations

'''
Host 192.168.0.11 has a user pentest which can login via SSH. The
password for this user has exactly nine characters, starts with pent ,
is a variation of the username and contains only lower-case letters
and 1 number. Find it.
'''

s = "pent"

fuckcrunch = []

for i in range(0,10):
    charset = "pents{}".format(i)
    pi = permutations(charset, 5);
    for j in pi:
        new = s
        for z in j:
            new = new + z
        fuckcrunch.append(new)

print(len(fuckcrunch))

with open('pentest3_psw_list.txt', 'w') as f:
    for i in fuckcrunch:
        i = i + "\n"
        f.write(i)
