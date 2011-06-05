import sys

file = open(sys.argv[1])

for line in file:
    if line.startswith('['):
        print line.rstrip()
