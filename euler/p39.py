'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?'''

import sys


def main():
    maxp = int(sys.argv[1])

    total_max = 0
    for p in range(3, maxp+1):
        current_value = 0
        current_solutions = []
        for a in range(1,p/2):
            for b in range(1,p/2):
                c = p - a - b
                if c*c == a*a + b*b:
                    current_value += 1
                    current_solutions.append((a,b,c))
        if current_value > total_max:
            total_max = current_value
            print 'current maximum for p={0} - {1}: {2}'.format(p, current_value, current_solutions)



if __name__ == '__main__':
    main()
