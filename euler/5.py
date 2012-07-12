import psyco
psyco.full()

i = 20

while True:
    i += 20
    for div in range(1,21):
        if i % div:
            break
    if div == 20 and not (i % div):
        print "Number %d is evenly divisible by 1-20!" % i
        break
    if not i % 10000000:
        print "Current i=%d" % i

#print "Number %d is evenly divisible by 1-20!" % i