def spin(l, length):
    return l[-length:] + l[:-length]

def exchange(l, a, b):
    l[a], l[b] = l[b], l[a]

def partner(l, a, b):
    index_a = l.index(a)
    index_b = l.index(b)
    exchange(l, index_a, index_b)

def main():
    input = open('december16_input.txt').readline().split(",")
    l = [chr(i) for i in range(ord("a"), ord("q"))]
    print(part1(l[:], input))
    print(part2(l[:], input, int(1e9)))

# @profile
def dance(l, input):
    for action in input:
        if action[0] == 's':
            l = spin(l, int(action[1:]))
        elif action[0] == 'x':
            indices = action[1:].split('/')
            exchange(l, int(indices[0]), int(indices[1]))
        elif action[0] == 'p':
            partner(l, action[1], action[-1])
        else:
            assert False
    return l

def part1(l, input):
    return(''.join(dance(l, input)))

def part2(l, input, iterations):
    memo = {}
    counter = 0
    original_list = l[:]
    while True:
        input_string = ''.join(l)
        if input_string in memo:
            assert input_string == ''.join(original_list)
            break
        else:
            l = dance(l, input)
            output_string = ''.join(l)
            memo[input_string] = output_string
        counter += 1
    left = int(iterations) % counter
    l = ''.join(original_list)
    for i in range(left):
        l = memo[l]
    return l

def test_part1():
    input = ["s1", "x3/4", "pe/b"]
    l = [c for c in "abcde"]
    assert part1(l, input) == "baedc"
    assert part2(l, input, int(1e9)) == "abcde"

def test_part2():
    input = open('december16_input.txt').readline().split(",")
    l = [chr(i) for i in range(ord("a"), ord("q"))]
    with_part2 = part2(l[:], input, 100)
    for _ in range(100):
        l = dance(l, input)
    assert with_part2 == ''.join(l)

if __name__ == '__main__':
    main()
