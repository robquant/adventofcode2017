def shift_forward(l, pos):
    return l[pos:] + l[:pos]

def reverse(l, length):
    return list(reversed(l[:length:])) + l[length:]

def shift_back(l, pos):
    return l[-pos:] + l[:-pos]

def pinch_and_twist(l, pos, length):
    temp = shift_forward(l, pos)
    temp = reverse(temp, length)
    return shift_back(temp, pos)

def hash_round(l, lengths, pos, skip_size):
    for length in lengths:
        l = pinch_and_twist(l, pos, length)
        pos = (pos + length + skip_size) % len(l)
        skip_size += 1
    return l, pos, skip_size

def densify(l):
    dense_hash = []
    for i in range(16):
        h = 0
        for el in l[i * 16:(i + 1) * 16]:
            h ^= el
        dense_hash.append(h)
    return dense_hash

def main():
    input = "120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113"
    input_part1 = [int(n) for n in input.split(',')]
    l = list(range(256))
    skip_size = 0
    pos = 0
    l, _, _ = hash_round(l, input_part1, pos, skip_size)
    print(l[0] * l[1])
    
    # Part2
    standard_suffix = [17, 31, 73, 47, 23]
    input_part2 = [ord(c) for c in input]
    input_part2 += standard_suffix
    l = list(range(256))
    skip_size = 0
    pos = 0
    for _ in range(64):
        l, pos, skip_size = hash_round(l, input_part2, pos, skip_size)
    dense_hash = densify(l)
    fmt = "%02x"*16
    print(fmt%tuple(dense_hash))


if __name__ == '__main__':
    main()