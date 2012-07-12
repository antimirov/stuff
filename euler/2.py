import psyco
psyco.full()

f_list = [1,2]

while True:
    fib = f_list[-2] + f_list[-1]
    if fib > 1000000: break
    f_list.append(fib)

f = [x for x in f_list if not x%2]
print sum(f)
