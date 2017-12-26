from collections import namedtuple

Pos = namedtuple("Pos", ("x", "y"))
Dir = namedtuple("Dir", ("x", "y"))

def turn_left(direction):
    return Dir(-direction.y, direction.x)

def turn_right(direction):
    return Dir(direction.y, -direction.x)

def infected(field, pos):
    return field[pos.y][pos.x] == '#'

def infect(field, pos):
    field[pos.y][pos.x] = '#'

def clean(field, pos):
    field[pos.y][pos.x] = '.'

def step(field, pos, direction):
    if infected(field, pos):
        print("Turning right: ", direction)
        direction = turn_right(direction)
        print(direction)
        clean(field, pos)
    else: # clean
        print("Turning left: ", direction)
        direction = turn_left(direction)
        print(direction)
        infect(field, pos)
    pos = Pos(pos.x + direction.x, pos.y + direction.y)
    print("Infected: ", infected(field, pos))
    return pos, direction

def part1(input):
    l = len(input) // 2
    pos = (l, l)

def load(fname):
    input = [list(line.rstrip('\n')) for line in open(fname)]
    return input

def test_part1():
    input = load("test.txt")
    pos = Pos(4, 4)
    direction = Dir(0, 1)
    for _ in range(4):
        pos, direction = step(input, pos, direction)
        print_field(input, pos)
        print('--')

def print_field(field, pos):
    for i, line in enumerate(field):
        if i == pos.y:
            print(' '.join(line[:pos.x]) + '[' + line[pos.x] + ']' + ' '.join(line[pos.x+1:]))
        else:
            print(' '.join(line))

def main():
    # input = load('december22_input.txt')
    test_part1()

if __name__ == '__main__':
    main()