import sys

'''Usage python compare-cogs.py <file1> <file2>'''

def read_In_Cogs(cog_file):
    cog_dict = {}
    input = open(cog_file, 'r')
    set_of_cogs = set()
    for n, line in enumerate(input):
        if line.startswith('COG'):
            line = line.rstrip().split('\t')
            cog_id = line[0]
            set_of_cogs.add(cog_id)
            cog_name = line[1]
            cog_count = int(line[2])
            if cog_dict.has_key(cog_id):
                cog_dict[cog_id][1] += cog_count
            else:
                cog_dict[cog_id] = [cog_name, cog_count]
    input.close()
    return set_of_cogs, cog_dict

if __name__ == '__main__': 
    first_file = sys.argv[1]
    second_file = sys.argv[2]
    print 'Reading in ', first_file
    first_file_cog_set, first_file_dict = read_In_Cogs(first_file)
    print 'Reading in ', second_file
    second_file_cog_set, second_file_dict = read_In_Cogs(second_file)
    intersection = first_file_cog_set.intersection(second_file_cog_set)
    first_file_only = first_file_cog_set.difference(second_file_cog_set)
    second_file_only = second_file_cog_set.difference(first_file_cog_set)
    print '---------------------'
    print 'intersection =', len(intersection)
    print first_file, ' = ', len(first_file_only)
    print second_file, ' = ', len(second_file_only)

    print '%s only' % first_file
    print '---------------------'
    for item in first_file_only:
        print '%s\t%s\t%d' % (item, first_file_dict[item][0], first_file_dict[item][1])
        
    print '%s only' % second_file
    print '---------------------'
    for item2 in second_file_only:
        print '%s\t%s\t%d' % (item2, second_file_dict[item2][0], second_file_dict[item2][1])
                    
