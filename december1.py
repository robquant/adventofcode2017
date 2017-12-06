def test_captcha_part1():
    assert captcha("1122", next_digit_wrap) == 3
    assert captcha("1111", next_digit_wrap) == 4
    assert captcha("1234", next_digit_wrap) == 0
    assert captcha("91212129", next_digit_wrap) == 9

def test_captcha_part2():
    assert captcha("1212", halfway_around_wrap) == 6
    assert captcha("1221", halfway_around_wrap) == 0
    assert captcha("123425", halfway_around_wrap) == 4
    assert captcha("123123", halfway_around_wrap) == 12
    assert captcha("12131415", halfway_around_wrap) == 4


def next_digit_wrap(length, index):
    return (index + 1) % length

def halfway_around_wrap(length, index):
    assert length % 2 == 0
    return (index + (length // 2)) % length

def captcha(number, compare_to):
    sum = 0
    for i in range(len(number)):
        if number[i] == number[compare_to(len(number), i)]:
            sum += int(number[i])
    return sum

def main():
    input = open("december1_input.txt").readline().strip()
    print(captcha(input, next_digit_wrap))
    print(captcha(input, halfway_around_wrap))

if __name__ == '__main__':
    main()