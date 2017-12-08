from collections import defaultdict

registers = defaultdict(int)

def compare(regname, op, value):
    if op == '<':
        return registers[regname] < value
    elif op =='<=':
        return registers[regname] <= value
    if op == '>':
        return registers[regname] > value
    elif op =='>=':
        return registers[regname] >= value
    if op == '==':
        return registers[regname] == value
    elif op =='!=':
        return registers[regname] != value
    else:
        raise ValueError("Unknown operation {}".format(op))

def change_register(regname, op, value):
    if op == 'inc':
        registers[regname] += value
        return
    elif op == 'dec':
        registers[regname] -= value
        return
    raise ValueError("Unknown operation {}".format(op))

def main(input):
    highest_ever = 0
    for line in input:
        items = line.split(' ')
        input_register = items[0]
        op = items[1]
        assert op == 'inc' or op == 'dec'
        op_value = int(items[2])
        if_ = items[3]
        assert if_ == 'if'
        comp_register = items[4]
        comp_op = items[5]
        assert comp_op in ('<', '<=', '>', '>=', '==', '!=')
        comp_val = int(items[6])
        if compare(comp_register, comp_op, comp_val):
            change_register(input_register, op, op_value)
        highest_ever = max(highest_ever, registers[input_register])
    print(max(registers.values()), highest_ever)


if __name__ == '__main__':
    input = open("december8_input.txt").readlines()
    main(input)
