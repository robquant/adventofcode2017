from collections import deque

def find_group(mappings, start):
    reachable = set()
    checked = set()
    reachable.add(start)
    checked.add(start)
    work = deque()
    for item in mappings[start]:
        work.append(item)
        reachable.add(item)
    while len(work) > 0:
        item = work.popleft()
        reachable.add(item)
        if not item in checked:
            for target in mappings[item]:
                work.append(target)
        checked.add(item)
    return reachable


def main():
    input = open("december12_input.txt").readlines()
    mappings = {}
    for line in input:
        items = line.split(' ')
        start = int(items[0])
        targets = [int(item.rstrip(',')) for item in items[2:]]
        mappings[start] = targets
    
    reachable = find_group(mappings, 0)
    print(len(reachable))

    groups = 1
    not_checked = set(mappings.keys()).difference(reachable)
    while len(not_checked) > 0:
        item = not_checked.pop()
        reachable = find_group(mappings, item)
        groups += 1
        not_checked = not_checked.difference(reachable)
    print(groups)
        
    

if __name__ == '__main__':
    main()
