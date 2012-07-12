import sys
import psyco
psyco.full()

def func():
    i=0
    while True:
        i += 1
        j = i / 17
        z = j**2
        if z == 346020415225:
            print 123
            sys.exit(0)

func()
