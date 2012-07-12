import time

t1 = time.time()


s=0
#s = []

for i in xrange(1,1000000):
    if not (i % 3 and i % 5):
#        s.append(i)
        s += i

#print sum(s)
print s

t2 = time.time()

print "time is %f" % (t2 - t1)