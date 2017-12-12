from collections import deque

def main():
    input = open("december12_input.txt").readlines()
    mappings = {}
    for line in input:
        items = line.split(' ')
        start = int(items[0])
        targets = [int(item.rstrip(',')) for item in items[2:]]
        mappings[start] = targets
    reachable = set()
    checked = set()
    reachable.add(0)
    checked.add(0)
    work = deque()
    for item in mappings[0]:
        work.append(item)
        reachable.add(item)
    while len(work) > 0:
        item = work.popleft()
        reachable.add(item)
        if not item in checked:
            for target in mappings[item]:
                work.append(target)
        checked.add(item)
    print(len(reachable))

if __name__ == '__main__':
    main()
