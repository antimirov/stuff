import sys
import psyco
psyco.full()

primes = [2]
current = primes[-1]
found = 1

while True:
    divides = False
    current += 1
    for i in primes:
        if not current%i:
            divides = True
            break

    if not divides:
        primes.append(current)
        found += 1
        if found == 10001:
            print current
            sys.exit(0)

