from collections import namedtuple

Pos = namedtuple("Pos", ("x", "y"))
Dir = namedtuple("Dir", ("x", "y"))

def turn_left(direction):
    return Dir(-direction.y, direction.x)

def turn_right(direction):
    return Dir(direction.y, -direction.x)

def infected(field, pos):
    return field[len(field) - pos.y][pos.x] == '#'

def infect(field, pos):
    field[len(field) - pos.y][pos.x] = '#'

def clean(field, pos):
    field[len(field) - pos.y][pos.x] = '.'

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

def part1(input):
    l = len(input) // 2
    pos = Pos(l, l)
    direction = Dir(0, 1)
    print(run(input, pos, direction, 10000))

def load(fname):
    input = [list(line.rstrip('\n')) for line in open(fname)]
    return input

def test_part1():
    input = load("test.txt")
    pos = Pos(4, 4)
    direction = Dir(0, 1)
    assert run(input, pos, direction, 70) == 41

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

def print_field(field, pos):
    for i, line in enumerate(field):
        if i == len(field) - pos.y:
            print(' '.join(line[:pos.x]) + '[' + line[pos.x] + ']' + ' '.join(line[pos.x+1:]))
        else:
            print(' '.join(line))

def main():
    input = load('december22_input.txt')
    part1(input)

if __name__ == '__main__':
    main()