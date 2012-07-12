import sys


d = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'one thousand'
}


def num_21_99towords(n):
    if n in d:
        return d[n]
    n1 = n % 10
    n2 = n - n1
    return d[n2]+'-'+d[n1]


def num_101_999towords(n):
    n3 = n / 100
    return d[n3] + ' hundred' + (' and ' + num_21_99towords(n % 100) if n % 100 else '')


def num2words(n):
    if n in d:
        return d[n]
    
    if n <= 99:
        return num_21_99towords(n)
    
    if n >= 100:
        return num_101_999towords(n)


def main():
    #print num2words(int(sys.argv[1]))
    c = 0
    for i in range(1, 1000+1):
        #print i, num2words(i)
        c += len(num2words(i).replace('-', '').replace(' ', ''))
    print c

if __name__ == '__main__':
    main()
