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

def knot_hash(input_string):
    standard_suffix = [17, 31, 73, 47, 23]
    input_part2 = [ord(c) for c in input_string]
    input_part2 += standard_suffix
    l = list(range(256))
    skip_size = 0
    pos = 0
    for _ in range(64):
        l, pos, skip_size = hash_round(l, input_part2, pos, skip_size)
    dense_hash = densify(l)
    return dense_hash