from collections import namedtuple, defaultdict
import time

Pos = namedtuple("Pos", ("x", "y"))
Dir = namedtuple("Dir", ("x", "y"))

def turn_left(direction):
    return Dir(-direction.y, direction.x)

def turn_right(direction):
    return Dir(direction.y, -direction.x)

def reverse(direction):
    return Dir(-direction.x, -direction.y)

def infected(field, pos):
    return field[pos] == '#'

def infect(field, pos):
    field[pos] = '#'

def clean(field, pos):
    field[pos] = '.'

def weaken(field, pos):
    field[pos] = 'W'

def weakened(field, pos):
    return field[pos] == 'W'

def flag(field, pos):
    field[pos] = 'F'

def flagged(field, pos):
    return field[pos] == 'F'

def step_part1(field, pos, direction):
    if infected(field, pos):
        direction = turn_right(direction)
        clean(field, pos)
        did_infect = False
    else: # clean
        direction = turn_left(direction)
        infect(field, pos)
        did_infect = True
    pos = Pos(pos.x + direction.x, pos.y + direction.y)
    return pos, direction, did_infect


def step_part2(field, pos, direction):
    did_infect = False
    if weakened(field, pos):
        infect(field, pos)
        did_infect = True
    elif infected(field, pos):
        flag(field, pos)
        direction = turn_right(direction)
    elif flagged(field, pos):
        clean(field, pos)
        direction = reverse(direction)
    else:
        direction = turn_left(direction)
        weaken(field, pos)
    pos = Pos(pos.x + direction.x, pos.y + direction.y)
    return pos, direction, did_infect


def part1(input, pos):
    direction = Dir(0, 1)
    print(run(input, pos, direction, 10000, step_part1))

def part2(input, pos):
    direction = Dir(0, 1)
    print(run(input, pos, direction, int(10e6), step_part2))

def load(fname):
    input = [list(line.rstrip('\n')) for line in open(fname)]
    field = defaultdict(lambda: '.')
    for row, line in enumerate(reversed(input)):
        for col, el in enumerate(line):
            field[Pos(col, row)] = el
    return field

def test_part1():
    input = load("test.txt")
    pos = Pos(4, 3)
    direction = Dir(0, 1)
    assert run(input, pos, direction, 10000, step_part1, debug=False) == 5587

def test_part2():
    input = load("test.txt")
    pos = Pos(4, 3)
    direction = Dir(0, 1)
    assert run(input, pos, direction, int(10e6), step_part2, debug=False) == 2511944


def run(field, pos, direction, steps, step, debug=False):
    infection_counter = 0
    for _ in range(steps):
        pos, direction, did_infect = step(field, pos, direction)
        if did_infect:
            infection_counter += 1
        if debug:
            print_field(field, pos)
            print('--')
    return infection_counter

def print_field(field, cursor_pos, size=10):
    for row in range(size, -1, -1):
        if cursor_pos.y == row:
            line = ' '.join(field[Pos(col, row)] for col in range(cursor_pos.x))
            line += '[' + field[cursor_pos] + ']' 
            line += ' '.join(field[Pos(col, row)] for col in range(cursor_pos.x + 1, size))
            print(line)
        else:
            print(' '.join(field[Pos(col, row)] for col in range(size)))

def main():
    #test_part1()
    start = time.time()
    input = load('december22_input.txt')
    l = int(len(input)**0.5)//2
    pos = Pos(l, l) 
    part1(input.copy(), pos)
    part2(input.copy(), pos)
    print("That took %4.3f seconds"%(time.time() - start))

if __name__ == '__main__':
    main()