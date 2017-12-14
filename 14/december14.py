from itertools import chain
from knot_hash import knot_hash

from collections import deque

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

def neighbours(indices, maxindex):
    n = []
    if indices[0] > 0:
        n.append((indices[0] - 1, indices[1]))
    if indices[0] < maxindex:
        n.append((indices[0] + 1, indices[1]))
    if indices[1] > 0:
        n.append((indices[0], indices[1] - 1))
    if indices[1] < maxindex:
        n.append((indices[0], indices[1] + 1))
    return n

def find_group(fields, start):
    assert fields[start[0]][start[1]] == '1'
    reachable = set()
    checked = set()
    reachable.add(start)
    checked.add(start)
    work = deque()
    for neighbour in neighbours(start, 127):
        if fields[neighbour[0]][neighbour[1]] == '1':
            work.append(neighbour)
            reachable.add(neighbour)
    while len(work) > 0:
        item = work.popleft()
        if not item in checked:
            for neighbour in neighbours(item, 127):
                if fields[neighbour[0]][neighbour[1]] == '1':
                    work.append(neighbour)
                    reachable.add(neighbour)
        checked.add(item)
    return reachable

def part2(key):
    hashes = defrag(key)
    fields = []
    for hash in hashes:
        fields.append(list(''.join((bin(h)[2:]).rjust(8, '0') for h in hash)))
    
    groups = 0
    not_checked = set((i, j) for i in range(128) for j in range(128) if fields[i][j] == '1')
    while len(not_checked) > 0:
        item = not_checked.pop()
        reachable = find_group(fields, item)
        groups += 1
        not_checked = not_checked.difference(reachable)
    return groups
    

def test_part1():
    key = 'flqrgnkx'
    one_sum = part1(key)
    assert one_sum == 8108

def test_part2():
    key = 'flqrgnkx'
    assert part2(key) == 1242

def main():
    key = 'ffayrhll'
    print(part1(key))
    print(part2(key))

if __name__ == '__main__':
    main()