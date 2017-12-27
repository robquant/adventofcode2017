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

def step(field, pos, direction):
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

def part1(input, pos):
    direction = Dir(0, 1)
    print(run(input, pos, direction, 10000))

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
    assert run(input, pos, direction, 10000, debug=False) == 5587

def run(field, pos, direction, steps, debug=False):
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
    part1(input, pos)
    print("That took %4.3f seconds"%(time.time() - start))

if __name__ == '__main__':
    main()