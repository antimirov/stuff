import psyco
psyco.full()


def func9():
    for a in range(500,1000):
        for b in range(1,500):
            c = 1000 - a - b
            if (a*a + b*b) == c*c:
                print a*b*c, a, b, c 



func9()
