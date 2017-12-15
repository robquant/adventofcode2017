from itertools import islice, starmap
from functools import reduce
from operator import add

import sys
if sys.version_info[0] == 2:
    from itertools import izip, ifilter
    zip = izip
    filter = ifilter

def main():
    part1()
    part2()

def generator(start, factor):
    n = start
    while True:
        n = (n * factor) % 2147483647
        yield n

def judge(a, b):
    return (a & 65535) == (b & 65535)

def part1():
    gen_a = generator(634, 16807)
    gen_b = generator(301, 48271)
    gen_a = islice(gen_a, int(40e6))
    gen_b = islice(gen_b, int(40e6))
    print(reduce(add, starmap(judge, zip(gen_a, gen_b))))

def part2():
    gen_a = filter(lambda n: n % 4 == 0, generator(634, 16807))
    gen_b = filter(lambda n: n % 8 == 0, generator(301, 48271))
    gen_a = islice(gen_a, int(5e6))
    gen_b = islice(gen_b, int(5e6))
    print(reduce(add, starmap(judge, zip(gen_a, gen_b))))

if __name__ == '__main__':
    main()
