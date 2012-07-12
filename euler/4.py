#import psyco
#psyco.full()
import sys


max = 0
digits = None
for i in range(999, 0, -1):
    for j in range(999, 316, -1):
        product = i*j
        if product > 100000:
            sproduct = str(product)
            l = len(sproduct)/2
            s1 = sproduct[:l]
            s2 = sproduct[l:]
            s2 = s2[::-1]
            if s1 == s2:
                if product > max:
                    max = product
                    digits = (i, j)

print max, "=", digits[0], "*", digits[1]
