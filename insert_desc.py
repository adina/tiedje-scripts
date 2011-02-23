#!/usr/bin/python

import sys

if len(sys.argv) != 4:
	print "USAGE: insert_desc.py <desc_file> <in_blast> <out_blast>"
	sys.exit(1)

descriptions = dict()
for line in open(sys.argv[1]):
	lexemes = line.strip().split()
	descriptions[lexemes[0]] = " ".join(lexemes[1:])

out = open(sys.argv[3], "w")
for line in open(sys.argv[2]):
	lexemes = line.strip().split("\t")
	if len(lexemes) != 12:
		continue

	lexemes.insert(2, descriptions[lexemes[1]])
	out.write("%s\n" % ("\t".join(lexemes)))
