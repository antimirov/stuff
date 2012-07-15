# sum of amicable pairs

import sys
import math

def divisors(n):
    if n == 0: return []
    if n == 1: return [1]
    
    l = [1]
    for i in range(2, int(round(math.sqrt(n)))+1):
        if n % i == 0:
            l.append(i)
            reverse_divisor = n/i
            if reverse_divisor != i:
                l.append(n/i)
    return l


def main():
    s = set()
    for a in range(1, 10000):
        b = sum(divisors(a))
        sum_b = sum(divisors(b))
        if a != b and a == sum_b:
            print 'BINGO', a, b
            s.add(tuple(sorted([a,b])))
    
    print sum([a+b for a,b in s])


if __name__ == '__main__':
    main()
