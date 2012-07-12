import psyco
psyco.full()
import sys
import math


class P:

    def num_fract(self,num):

        fracts = 1
        divider = 2
        max_num = math.sqrt(num)

        while divider <= max_num:
            if (num % divider) == 0:
                fracts += 2
            divider += 1

        fracts += 1
        return fracts


    def main(self,target):
        num_fract = self.num_fract 
        curr_tr = i = 1
        while True:
            i += 1
            if (i % 1000) == 0:
                sys.stdout.write("\rProgress: %d    " % i)
                sys.stdout.flush()

            curr_tr += i
            num = num_fract(curr_tr)
            if num > target:
                print "Number of fractions: %d\ni: %d\ncurrent triangle: %d\n" % (num, i, curr_tr)
                break
        


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    p = P()
    p.main(int(sys.argv[1]))
