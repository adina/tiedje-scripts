import sys

rast_file = open(sys.argv[1], 'r')

d_files = {'4462228.3':'MSR2_Hiseq', '4462227.3':'MMR2_Hiseq', '4462240.3':'MMR2', '4462242.3':'MSB2', '4462243.3':'MSR1', '4462237.3':'MMB2', '4462246.3':'WSR2', '4462241.3':'MSB1', '4462239.3':'MMR1', '4462245.3':'WSR1', '4462236.3':'MMB1', '4462244.3':'MSR2', '4462226.3':'MSR1_Hiseq', '4462224.3':'MMB1_Hiseq', '4462059.3':'MSB1_Hiseq', '4462016.3':'MMR1_Hiseq'}
 
d = {}
d_cog_info = {}
for n, line in enumerate(rast_file):
    if n > 0:
        list = []
        line = line.rstrip().split('\t')
        METAID = line[0]
        LEVEL1 = line[1]
        LEVEL2 = line[2]
        FUNCTION = line[3]
        ID = line[4]
        ABUND = line[5]
        AVG = line[6]
        IDENT = line[7]
        ALN_LEN = line[8]
        N_PROTEINS = line[9]
        list = [METAID, ABUND]
        d_cog_info[ID]=[LEVEL1, LEVEL2, FUNCTION]
        if d.has_key(ID):
            d[ID].append(list)
        else:
            d[ID]=[list]
#print d
#print d_cog_info
fp = open(sys.argv[2], 'w')

sorted_keys = sorted(d.keys())
for key in sorted_keys:
    sorted_values = sorted(d[key], key = lambda x: x[0])
    fp.write('%s' % key)
    for i in range(0, len(sorted_values)):
        print sorted_values[i]
        fp.write('\t%d' % int(sorted_values[i][1]))
    fp.write('\n')
    
