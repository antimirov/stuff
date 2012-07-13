
# 18. triangle task


def main():
    f = open('18.dat').read()
    d = [ map(int, line.split(' ')) for line in open('18.dat').read().strip().split('\n') ]
    print d

    max_path = [max(row) for row in d]
    print max_path, '=', sum(max_path)
    


if __name__ == '__main__':
    main()
