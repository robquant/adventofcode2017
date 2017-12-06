def part2(input):
    checksum = 0
    for line in input:
        numbers = [int(n) for n in line.strip('\n').split('\t')]
        do_break = False
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                n1 = numbers[i]
                n2 = numbers[j]
                if max(n1, n2) % min(n1, n2) == 0:
                    checksum += max(n1, n2)//min(n1, n2)
                    do_break = True
            if do_break:
                break
    print(checksum)

def part1(input):
    checksum = 0
    for line in input:
        numbers = [int(n) for n in line.strip('\n').split('\t')]
        checksum += max(numbers) - min(numbers)
    print(checksum)

if __name__ == '__main__':
    input = open("december2_input.txt").readlines()
    part1(input)
    part2(input)