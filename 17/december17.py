def main():
    print(part1())
    print(part2())

def part2():
    input = 312
    buffer = []
    pos = 0
    final = 0
    for n in range(int(50e6)):
        if n > 0:
            pos = (pos + input + 1) % n
        if pos == 0:
            final = n
    return final

def part1():
    input = 312
    buffer = []
    pos = 0
    for n in range(2018):
        if n > 0:
            pos = (pos + input + 1) % n
        buffer.insert(pos, n)
    return buffer[buffer.index(2017) + 1]

if __name__ == '__main__':
    main()
