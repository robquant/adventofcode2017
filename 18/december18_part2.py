from collections import defaultdict
from queue import deque

#     snd X sends value X to the other program
#     set X Y sets register X to the value of Y.
#     add X Y increases register X by the value of Y.
#     mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
#     mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
#     rcv X receives into X a value from the other program, FIFO queue
#     jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

# What is the value of the recovered frequency (the value of the most recently played sound) the first time a rcv instruction is executed with a non-zero value?



class Program():

    def __init__(self, program_id, program, receive_queue, send_queue):
        self.program = program
        self.registers = defaultdict(int)
        self.program_id = program_id
        self.registers['p'] = program_id
        self.receive_queue = receive_queue
        self.send_queue = send_queue
        self.ptr = 0
        self.send_counter = 0

    def get_op_value(self, op):
        if 'a' <= op <= 'z':
            return int(self.registers[op])
        return int(op)

    def send(self, value):
        self.send_queue.append(value)

    def can_receive(self):
        return len(self.receive_queue) > 0

    def receive(self):
        return self.receive_queue.popleft()

    def step(self):
        if self.ptr >= len(self.program):
            return False
        ins = self.program[self.ptr]
        # print(self.program_id, ins)
        command = ins[0]
        if command == 'snd':
            self.send(int(self.get_op_value(ins[1])))
            self.send_counter += 1
        elif command == 'set':
            self.registers[ins[1]] = self.get_op_value(ins[2])
        elif command == 'add':
            self.registers[ins[1]] = self.registers[ins[1]] + self.get_op_value(ins[2])            
        elif command == 'mul':
            self.registers[ins[1]] = self.registers[ins[1]] * self.get_op_value(ins[2])            
        elif command == 'mod':
            self.registers[ins[1]] = self.registers[ins[1]] % self.get_op_value(ins[2])            
        elif command == 'rcv':
            if self.can_receive():
                self.registers[ins[1]] = self.receive()
            else:
                return False
        elif command == 'jgz':
            if self.get_op_value(ins[1]) > 0:
                self.ptr += self.get_op_value(ins[2])
                return True
        self.ptr += 1
        return True

def main():
    input = [line.rstrip('\n').split(' ') for line in open("december18_input.txt")]
    # input = [line.rstrip('\n').split(' ') for line in open("test.txt")]
    queue_0_1 = deque()
    queue_1_0 = deque()
    p0 = Program(0, input, queue_1_0, queue_0_1)
    p1 = Program(1, input, queue_0_1, queue_1_0)
    while True:
        while p0.step():
            pass
        while p1.step():
            pass
        if not p0.can_receive():
            break

    print(p1.send_counter)

if __name__ == '__main__':
    main()