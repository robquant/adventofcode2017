def total_score(input):
    garbage_mode = False
    bracket_level = 1
    assert input[0] ==  '{'
    assert input[-1] ==  '}'
    index = 1
    score = 1 # outermost group
    garbage_characters = 0
    while index < len(input) - 1:
        symbol = input[index]
        if symbol == '!':
            index += 2
            continue
        if garbage_mode:
            if symbol == '>':
                garbage_mode = False
            else:
                garbage_characters += 1
        else: # normal mode
            if symbol == '<':
                garbage_mode = True
            elif symbol == '{':
                bracket_level += 1
            elif  symbol == '}':
                score += bracket_level
                bracket_level -= 1
        index += 1
    assert bracket_level == 1
    return score, garbage_characters


def main(input):
    print(total_score(input))


def test_total_score():
    assert total_score("{}")[0] == 1
    assert total_score("{{{}}}")[0] == 6
    assert total_score("{{},{}}")[0] == 5
    assert total_score("{{{},{},{{}}}}")[0] == 16
    assert total_score("{<a>,<a>,<a>,<a>}")[0] == 1
    assert total_score("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
    assert total_score("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
    assert total_score("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

    assert total_score("{<>}")[1] == 0
    assert total_score("{<random characters>}")[1] == 17
    assert total_score("{<<<<>}")[1] == 3
    assert total_score("{<{!>}>}")[1] == 2
    assert total_score("{<!!>}")[1] == 0
    assert total_score("{<!!!>>}")[1] == 0
    assert total_score("{<{o'i!a,<{i<a>}")[1] == 10



if __name__ == '__main__':
    input = open("december9_input.txt").readline().rstrip('\n')
    main(input)