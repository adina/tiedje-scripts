import sys

rast_file = open(sys.argv[1], 'r')

d_files = {'4462228.3':'MSR2_Hiseq', '4462227.3':'MMR2_Hiseq', '4462240.3':'MMR2', '4462242.3':'MSB2', '4462243.3':'MSR1', '4462237.3':'MMB2', '4462246.3':'WSR2', '4462241.3':'MSB1', '4462239.3':'MMR1', '4462245.3':'WSR1', '4462236.3':'MMB1', '4462244.3':'MSR2', '4462226.3':'MSR1_Hiseq', '4462224.3':'MMB1_Hiseq', '4462016.3':'MMR1_Hiseq', '4462059.3':'MSB1_Hiseq'}

d_files_list = []
d_files_keys = sorted(d_files.keys())

for i in d_files_keys:
    d_files_list.append([i, 0])

d = {}
d_list = {}
for n, line in enumerate(rast_file):
    if n > 0:
        line = line.rstrip().split('\t')
        METAID = line[0]
        LEVEL1 = line[1]
        LEVEL2 = line[2]
        LEVEL3 = line[3]
        FUNCTION = line[4]
        ABUND = line[5]
        AVG = line[6]
        IDENT = line[7]
        ALN_LEN = line[8]
        N_PROTEINS = line[9]
        UNIQUE_ID = LEVEL1+'|'+LEVEL2+'|'+ LEVEL3 + '|' + FUNCTION
        print METAID
        index = d_files_keys.index(METAID)

        if d.has_key(UNIQUE_ID):
            d[UNIQUE_ID][index] = [METAID, ABUND]
            #print '1', d
        else:
            d_files_list = []
            for i in d_files_keys:
                d_files_list.append([i, 0])
            d[UNIQUE_ID]=d_files_list
            #print d_files_list

            #print d_files_keys
            #print METAID, index
            #print d[UNIQUE_ID][index]
            #print [METAID, ABUND]
            d[UNIQUE_ID][index]=[METAID, ABUND]
            #print '2', d
#print d            
#print d_cog_info
fp = open(sys.argv[2], 'w')

sorted_keys = sorted(d.keys())

for key in sorted_keys:
    fp.write('%s' % key)
    for i in d[key]:
        #print key, i[1]
        fp.write('\t%d' % int(i[1]))
    fp.write('\n')
for filename in d_files_keys:
    print d_files[filename], filename
