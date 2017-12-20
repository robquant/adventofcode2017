import numpy as np
from numba import autojit


def parse_vector(vec):
    return [int(v) for v in vec.split(',')]


def parse_line(line):
    pos = 0
    res = []
    for _ in range(3):
        eq = line.find("=", pos)
        res.append(parse_vector(line[eq + 2:line.find(">", eq)]))
        pos = eq + 2
    return res


def step(pos, vel, acc):
    vel += acc
    pos += vel


@autojit
def collisions(X):
    M = X.shape[0]
    assert X.shape[1] == 3
    select = np.ones(M, dtype=np.bool)
    for i in range(M):
        for j in range(i + 1, M):
            if X[i, 0] - X[j, 0] == 0 and \
               X[i, 1] - X[j, 1] == 0 and \
               X[i, 2] - X[j, 2] == 0:
                select[i] = 0
                select[j] = 0
    return select


def closest_particle(pos):
    return np.argmin(np.abs(pos).sum(axis=1))


def part1(pos, vel, acc):
    count = 0
    max_count = int(1e6)
    while count < max_count:
        step(pos, vel, acc)
        count += 1
    closest = closest_particle(pos)
    print(closest)


def part2(pos, vel, acc):
    count = 0
    max_count = int(10000)
    while count < max_count:
        step(pos, vel, acc)
        select = collisions(pos)
        pos = pos[select]
        vel = vel[select]
        acc = acc[select]
        count += 1
    print(pos.shape[0])


def main():
    pos, vel, acc = [], [], []
    for line in open("december20_input.txt"):
        res = parse_line(line)
        pos.append(res[0])
        vel.append(res[1])
        acc.append(res[2])
    pos = np.array(pos, dtype=np.double)
    vel = np.array(vel, dtype=np.double)
    acc = np.array(acc, dtype=np.double)
    part1(pos.copy(), vel.copy(), acc.copy())
    part2(pos.copy(), vel.copy(), acc.copy())


if __name__ == '__main__':
    main()