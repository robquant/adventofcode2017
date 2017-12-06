def choose_bank_to_redist(banks):
    max_el = max(banks)
    return banks.index(max_el)


def part1(banks):
    counter = 0
    already_seen = {tuple(banks): counter}
    nbanks = len(banks)
    while True:
        counter += 1
        redist_bank = choose_bank_to_redist(banks)
        redist_amount = banks[redist_bank]
        banks[redist_bank] = 0
        current_bank = redist_bank
        for _ in range(redist_amount):
            current_bank = (current_bank + 1) % nbanks
            banks[current_bank] += 1
        if tuple(banks) in already_seen:
            return counter, counter - already_seen[tuple(banks)]
        already_seen[tuple(banks)] = counter


def main():
    input = list(map(int, open("december6_input.txt").readline().split('\t')))
    print(part1(input))


def test_part1():
    assert part1([0, 2, 7, 0]) == 5


if __name__ == '__main__':
    main()
