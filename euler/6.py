import psyco
psyco.full()

s = 0

for i in xrange(1,100+1):
    s += pow(i,2)

print s