def find_entry(field):
    for i, symbol in enumerate(field[0]):
        if symbol == '|':
            return (0, i)


def turn_left(dir):
    return (-dir[1], dir[0])


def turn_right(dir):
    return (dir[1], -dir[0])


def main():
    input = [
        list(iter(line.rstrip('\n'))) for line in open('december19_input.txt')
        if line != '\n'
    ]

    height = len(input)
    width = max((len(row) for row in input))
    field = []
    for row in input:
        if len(row) < width:
            field.append(row + [' '] * (width - len(row)))
        else:
            field.append(row)

    res = []
    pos = find_entry(field)
    dir = (1, 0)
    stepcounter = 1
    while field[pos[0]][pos[1]] != ' ':
        while 0 <= pos[0] < height and 0 <= pos[1] < width and field[pos[0]][pos[1]] != '+' and field[pos[0]][pos[1]] != ' ':
            if 'A' <= field[pos[0]][pos[1]] <= 'Z':
                res.append(field[pos[0]][pos[1]])
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            stepcounter += 1
        if pos[0] == height or pos[0] == -1 or pos[1] == width or pos[1] == -1 or field[pos[0]][pos[1]] == ' ':
            stepcounter -= 1
            break
        left = turn_left(dir)
        if 0 <= pos[0] + left[0] < height and 0 <= pos[1] + left[1] < width and \
            field[pos[0] + left[0]][pos[1] + left[1]] != ' ':
            dir = left
        else:
            dir = turn_right(dir)
            assert field[pos[0] + dir[0]][pos[1] + dir[1]] != ' '
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        stepcounter += 1
    print(''.join(res))
    print(stepcounter)


if __name__ == '__main__':
    main()