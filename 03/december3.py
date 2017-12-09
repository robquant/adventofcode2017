from collections import defaultdict

def manhattan_distance(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])

def find_layer(n):
    i = 0
    while n > 4 * i * i +1:
        i += 1
    return i

def step_to_coordinate(step):
    import pdb
    # pdb.set_trace()
    layer = find_layer(step)
    coord = (-layer, layer)
    value = 4 * layer * layer + 1
    if step >= value - 2 * layer:
        return (coord[0] + value - step, coord[1])
    coord = (coord[0] + 2 * layer, coord[1])
    value -= 2 * layer
    if step >= value - 2 * layer + 1:
        return (coord[0], coord[1] + (step - value))
    coord = (coord[0], coord[1] - 2 * layer + 1)
    value -= 2 * layer - 1
    if step >= value - 2 * layer + 1:
        return (coord[0] + step - value, coord[1])
    coord = (coord[0] - 2 * layer + 1, coord[1])
    value -= 2 * layer - 1
    if step >= value - 2 * layer:
        return (coord[0] , coord[1] + value - step)
    assert False

def neighbors(coord):
    return ((coord[0] - 1, coord[1] - 1), (coord[0] - 1, coord[1]), (coord[0] - 1, coord[1] + 1),
            (coord[0], coord[1] - 1), (coord[0], coord[1] + 1),
            (coord[0] + 1, coord[1] - 1), (coord[0] + 1, coord[1]), (coord[0] + 1, coord[1] + 1))

def part2(input):
    fields = defaultdict(int)
    n = 1
    value = 1
    fields[(0, 0)] = 1
    while value <= input:
        n += 1
        coord = step_to_coordinate(n)
        value = sum(fields[neighbor] for neighbor in neighbors(coord))
        fields[coord] = value
    return value

def main():
    input = 289326
    print(manhattan_distance(step_to_coordinate(input)))
    print(part2(input))

def test_part2():
    assert part2(142) == 147

def test_find_layer():
    assert find_layer(1) == 0
    assert find_layer(4) == 1
    assert find_layer(7) == 2
    assert find_layer(17) == 2
    assert find_layer(19) == 3

def test_step_to_coordinate():
    assert step_to_coordinate(2) == (1, 0)
    assert step_to_coordinate(4) == (0, 1)
    assert step_to_coordinate(7) == (-1, -1)
    assert step_to_coordinate(19) == (-2, 0)

if __name__ == '__main__':
    main()