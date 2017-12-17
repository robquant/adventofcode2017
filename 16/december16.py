def spin(l, length):
    return l[length:] + l[:length]

def exchange(l, a, b):
    l[a], l[b] = l[b], l[a]

def partner(l, a, b):
    index_a = l.index(a)
    index_b = l.index(b)
    exchange(l, index_a, index_b)

def main():
    input = open('december16_input.txt').readline().split(",")
    l = [chr(i) for i in range(ord("a"), ord("q"))]
    part1(l, input)

def part1(l, input):
    for action in input:
        if action[0] == 's':
            l = spin(l, int(action[1]))
        elif action[0] == 'x':
            indices = [int(n) for n in action[1:].split('/')]
            exchange(l, indices[0], indices[1])
        elif action[0] == 'p':
            partner(l, action[1], action[-1])
        else:
            assert False
    return(''.join(l))

def test_part1():
    input = ["s1", "x3/4", "pe/b"]
    l = [c for c in "abcde"]
    assert part1(l, input) == "baedc"

if __name__ == '__main__':
    main()