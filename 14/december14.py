from itertools import chain
from knot_hash import knot_hash

def defrag(key):
    hashes = []
    for number in range(128):
        row_key = key + "-%d"%number
        hash = knot_hash(row_key)
        hashes.append(hash)
    return hashes

def part1(key):
    hashes = defrag(key)
    one_sum = 0
    for item in chain.from_iterable(hashes):
        one_sum += (bin(item)[2:]).count('1')
    return one_sum

def test():
    key = 'flqrgnkx'
    one_sum = part1(key)
    assert one_sum == 8108

def main():
    key = 'ffayrhll'
    print(part1(key))

if __name__ == '__main__':
    main()