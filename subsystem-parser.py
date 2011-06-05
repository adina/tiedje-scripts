import sys



parsed_file = open(sys.argv[1], 'r')

d_files = {'4462228.3':'MSR2_Hiseq', '4462227.3':'MMR2_Hiseq', '4462240.3':'MMR2', '4462242.3':'MSB2', '4462243.3':'MSR1', '4462237.3':'MMB2', '4462246.3':'WSR2', '4462241.3':'MSB1', '4462239.3':'MMR1', '4462245.3':'WSR1', '4462236.3':'MMB1', '4462244.3':'MSR2', '4462226.3':'MSR1_Hiseq', '4462224.3':'MMB1_Hiseq', '4462016.3':'MMR1_Hiseq', '4462059.3':'MSB1_Hiseq'}

d_files_sorted = sorted(d_files.keys())
for key in d_files_sorted:
    print d_files[key], key

d = {}

for line in parsed_file:
    line = line.rstrip().split('\t', 1)
    id = line[0].split('|', 4)
    counts = line[1].split('\t')
    subsys = id[0]
    level1 = id[1]
    level2 = id[2]
    level3 = id[3]
    LEVEL = level3
    if d.has_key(LEVEL):
        d[LEVEL].append(counts)
    else:
        d[LEVEL] = [counts]

d2 = {}

sorted_keys = sorted(d.keys())

for key in sorted_keys:
    list = [0]*len(d_files.keys())
    for i in range(0, len(d[key])):
        for n, j in enumerate(d[key][i]):
            list[n] += int(j)
    d2[key]=list

fp = open(sys.argv[2], 'w')
for key in d2:
    fp.write('%s' % key)
    for i in d2[key]:
        fp.write('\t%d' % i)
    fp.write('\n')
