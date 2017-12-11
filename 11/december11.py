from collections import namedtuple

Axial = namedtuple("Axial", ["q", "r"])

def hex_distance(a, b):
    return (abs(a.q - b.q) 
          + abs(a.q + a.r - b.q - b.r)
          + abs(a.r - b.r)) / 2

def move_step(a, direction):
    if direction == 'n':
        return Axial(a.q, a.r - 1)
    elif direction == 'ne':
        return Axial(a.q + 1, a.r -1)
    elif direction == 'se':
        return Axial(a.q + 1, a.r)
    elif direction == 's':
        return Axial(a.q, a.r + 1)
    elif direction == 'sw':
        return Axial(a.q - 1, a.r + 1)
    elif direction == 'nw':
        return Axial(a.q - 1, a.r)
    else:
        assert False

def move_sequence(start, sequence):
    steps = [start]
    for move in sequence:
        steps.append(move_step(steps[-1], move))
    return steps

def test_sequence_distance():
    start = Axial(0, 0)
    end = move_sequence(start, ["ne","ne","ne"])
    assert hex_distance(start, end) == 3
    end = move_sequence(start, ["ne", "ne", "sw" ,"sw"])
    assert hex_distance(start, end) == 0
    end = move_sequence(start, ["ne", "ne", "s", "s"])
    assert hex_distance(start, end)  == 2
    end = move_sequence(start, ["se", "sw", "se", "sw", "sw"])
    assert hex_distance(start, end) == 3


def main():
    input = open("december11_input.txt").readline().rstrip('\n').split(',')
    start = Axial(0,0)
    steps = move_sequence(start, input)
    print(hex_distance(start, steps[-1]))
    print(max(hex_distance(step, start) for step in steps))

if __name__ == '__main__':
    main()