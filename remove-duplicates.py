#!/usr/bin/python

import sys

check_id2 = ''
for line in open(sys.argv[1]):
    check_id1 = line.split('\t')[0]
    if check_id1 != check_id2:
        print line.rstrip()
        check_id2 = check_id1
    else:
        continue

