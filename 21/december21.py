import numpy as np

def gen_patterns(pattern):
    patterns = [pattern]
    for _ in range(3):
        patterns.append(np.rot90(patterns[-1]))
    patterns.append(np.flipud(pattern))
    patterns.append(np.fliplr(pattern))
    patterns.append(np.rot90(np.flipud(pattern)))
    patterns.append(np.rot90(np.flipud(pattern), k=3))
    return patterns

def handle(field, replacement_table, in_size, out_size):
    size = field.shape[0]//in_size
    target_size = size * out_size
    target = np.empty((target_size, target_size), dtype=np.character)
    for i in range(size):
        for j in range(size):
            a = field[i*in_size:(i+1) * in_size, j * in_size:(j+1) * in_size]
            t = to_array(replacement_table[to_string(a)])
            target[i * out_size: (i+1) * out_size, j*out_size:(j+1) * out_size] = t
    return target

def to_string(pattern):
    return b''.join(pattern.ravel())

def to_array(pattern):
    if len(pattern) == 4:
        size = 2
    elif len(pattern) == 9:
        size = 3
    elif len(pattern) == 16:
        size = 4
    else:
        assert False
    return np.array(list(pattern), dtype=np.character).reshape(size, size)
     
def parse_pattern(pattern_str):
    inp, _, outp = pattern_str.split()
    inp = inp.replace('/', '' )
    outp = outp.replace('/', '' )
    return inp, outp    

def gen_replacement_table(patterns):
    replacement_table = {}
    for pattern in patterns:
        inp, outp = parse_pattern(pattern)
        inp_as_array = to_array(inp)
        for p in gen_patterns(inp_as_array):
            replacement_table[to_string(p)] = outp
    return replacement_table

def part1(pattern, replacement_patterns, iterations):
    replacement_table = gen_replacement_table(replacement_patterns)
    for _ in range(iterations):
        if pattern.shape[0] % 2 == 0:
            pattern = handle(pattern, replacement_table, 2, 3)
        elif pattern.shape[0] % 3 == 0:
            pattern = handle(pattern, replacement_table, 3, 4)
        else:
            assert False
    return np.sum(pattern == b'#')

def main():
    start = np.array(list(".#...####"), dtype=np.character).reshape(3,3)
    patterns = [line.rstrip('\n') for line in open('december21_input.txt')]
    print(part1(start.copy(), patterns, 5))
    print(part1(start.copy(), patterns, 18))

def test_part1():
    start = np.array(list(".#...####"), dtype=np.character).reshape(3,3)
    patterns = ["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"]
    assert part1(start, patterns, 2) == 12

if __name__ == '__main__':
    main()