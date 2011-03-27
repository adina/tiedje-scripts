#!/usr/bin/python

import sys

if len(sys.argv) != 4:
	print "USAGE: insert_cog_desc.py <desc_file> <in_cog> <out_cog>"
	sys.exit(1)

descriptions = dict()

for line in open(sys.argv[1], 'rU'):
	data = line.strip().split(' ', 2)
	cog_id = data[1]
	cog_abbrev = data[0][1:-1]
	cog_descr = data[2]
	descriptions[cog_id] = [cog_abbrev, cog_descr]

out = open(sys.argv[3], "w")
for n, line in enumerate(open(sys.argv[2], 'rU')):
	if n == 0:
		out.write('%s' % line)
	if n > 0:
		data2 = line.strip().split(',')
		data2.insert(1, descriptions[data2[0]][0])
		print data2
		out.write('%s\n' %','.join(data2))

