from collections import defaultdict

#     snd X plays a sound with a frequency equal to the value of X.
#     set X Y sets register X to the value of Y.
#     add X Y increases register X by the value of Y.
#     mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
#     mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
#     rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
#     jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

# What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?

def get_op_value(registers, op):
    if 'a' <= op <= 'h':
        return int(registers[op])
    return int(op)

def run(program):
    registers = defaultdict(int)
    registers['a'] = 1
    ptr = 0
    mul_counter = 0
    counter = 0
    while ptr < len(program):
        ins = program[ptr]
        if ptr == 10:
            print(registers['b'])
        # print(ptr, ins, registers)
        command = ins[0]
        if command == 'set':
            registers[ins[1]] = get_op_value(registers, ins[2])
        elif command == 'sub':
            registers[ins[1]] = registers[ins[1]] - get_op_value(registers, ins[2])            
        elif command == 'mul':
            registers[ins[1]] = registers[ins[1]] * get_op_value(registers, ins[2])            
            mul_counter += 1
        elif command == 'jnz':
            if get_op_value(registers, ins[1]) != 0:
                ptr += get_op_value(registers, ins[2])
                continue
        else:
            assert False, ins
        ptr += 1
    return mul_counter

def main():
    input = [line.rstrip('\n').split(' ') for line in open("december23_input.txt")]
    print(run(input))

if __name__ == '__main__':
    main()