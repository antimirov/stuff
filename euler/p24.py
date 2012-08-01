import itertools


c = 0
for comb in itertools.permutations('0123456789'):
    c+=1
    if c==1000000: print ''.join(comb)
