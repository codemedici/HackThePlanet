#!/usr/bin/env python

'''
onesixtyone can only read community string lists of max 32 lines...
this script takes a larger list and splits it chunks of 32, writing each chunk to a new file
'''

with open("wordlist-common-snmp-community-strings.txt", 'r') as f:
    lines = f.read().splitlines()

#http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

c = 1 # counter
for i in list(chunks(lines, 32)):
    with open("community_list_%d" % c, 'w') as f:
        for j in i:
            f.write("%s\n" % j)
    c = c + 1
