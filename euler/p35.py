'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

import sys
import itertools
from math import sqrt


def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for d in xrange(3, int(sqrt(n))+1, 2):
        if d*(n // d) == n:
            return False
    return True


def rotate(s):
    l = len(s)
    ss = s+s
    for i in range(len(s)):
        yield ss[i:l+i]


def main():
    primes = set()
    for n in range(2, int(sys.argv[1])+1):
        if is_prime(n):
            #print n
            primes.add(n)

    c = 0
    for p in primes:
        for n in rotate(str(p)):
            if int(n) not in primes:
                break
        else:
            c += 1
    print c


if __name__ == '__main__':
    main()
