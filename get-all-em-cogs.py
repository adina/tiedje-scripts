#! /usr/bin/env python

import sys

fp = open(sys.argv[1], 'w')
files = sys.argv[2:]

dict_files = {}

for file in files:
    dict_files[file] = {}
    dict_cogs = {}
    file_in = open(file, 'r')
    for n, line in enumerate(file_in):
        if n > 0:
            data = line.rstrip().split('\t')
            cog_id = data[0]
            count = data[1]
            descr = data[2]
            grouping = data[3]
            dict_cogs[cog_id] = count
    dict_files[file] = dict_cogs

files_alpha = sorted(dict_files.keys())
cogs_set = set()

'''gets all the cogs that exist in all files'''
for key in files_alpha:
    cogs_to_add = dict_files[key].keys()
    for cog in cogs_to_add:
        cogs_set.add(cog)
    cogs_set_sorted = sorted(cogs_set)

'''adds in the zeroes'''
for key in files_alpha:
    for each_cog in cogs_set_sorted:
        if dict_files[key].has_key(each_cog):
            continue
        else:
            dict_files[key][each_cog] = 0

'''goes and prints everything out in order'''
fp.write('COG')
for key in files_alpha:
    fp.write('\t%s' % key)
fp.write('\n')

for each_cog in cogs_set_sorted:
    fp.write('%s\t' % each_cog)
    for key in files_alpha: 
        fp.write('%s\t' % dict_files[key][each_cog])
    fp.write('\n')
'''fills in the empties with zeroes'''
'''dict[file_name] = {COG: info, COG: info}'''



        
    

