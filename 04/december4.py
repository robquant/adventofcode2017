from collections import Counter

def part2(input):
    counter = 0
    for line in input:
        if all(map(lambda v: v == 1, Counter((''.join(sorted(s)) for s in line.strip('\n').split())).values())):
            counter += 1
    return counter

def part1(input):
    counter = 0
    for line in input:
        if all(map(lambda v: v == 1, Counter(line.strip('\n').split()).values())):
            counter += 1
    return counter

def main():
    input = open("december4_input.txt").readlines()
    print(part1(input))
    print(part2(input))

if __name__ == '__main__':
    main()