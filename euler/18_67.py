# 18. triangle task

import sys


def main():
    d = [ map(int, line.split(' ')) for line in open(sys.argv[1]).read().strip().split('\n') ]

    for i in range(len(d)-2,-1,-1):
        for j in range(len(d[i])):
            max_path = max(d[i+1][j], d[i+1][j+1])
            d[i][j] = d[i][j] + max_path
    
    print d[0][0]


if __name__ == '__main__':
    main()
