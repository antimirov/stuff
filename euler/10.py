import sys
import psyco
psyco.full()

def func10():

    primes = [2,3]
    current = primes[-1]
    psum = sum(primes)
    found = 1

    while current <= 2000000:
        divides = False
        current += 2
        for i in primes:
            if not current%i:
                divides = True
                break

        if not divides:
            primes.append(current)
            psum += current


    print psum


func10()
