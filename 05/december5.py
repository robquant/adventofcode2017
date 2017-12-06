
def part2(input):
    counter = 0
    mem = [int(x) for x in input]
    ptr = 0
    while ptr < len(mem):
        counter += 1
        old_jump = mem[ptr]
        if old_jump >= 3:
            mem[ptr] -= 1
        else:
            mem[ptr] += 1
        ptr += old_jump
    return counter

def part1(input):
    counter = 0
    mem = [int(x) for x in input]
    ptr = 0
    while ptr < len(mem):
        counter += 1
        old_jump = mem[ptr]
        mem[ptr] += 1
        ptr += old_jump
    return counter

def main():
    input = open("december5_input.txt").readlines()
    print(part1(input))
    print(part2(input))

if __name__ == '__main__':
    main()