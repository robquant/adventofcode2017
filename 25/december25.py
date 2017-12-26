from enum import Enum
from collections import defaultdict

class State(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6

# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state C.
def stateA(tape, ptr):
    if tape[ptr] == 0:
        tape[ptr] = 1
        return State.B, ptr + 1
    else:
        tape[ptr] = 0
        return State.C, ptr - 1

# In state B:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state C.
def stateB(tape, ptr):
    if tape[ptr] == 0:
        tape[ptr] = 1
        return State.A, ptr - 1
    else:
        return State.C, ptr + 1

# In state C:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state D.
def stateC(tape, ptr):
    if tape[ptr] == 0:
        tape[ptr] = 1
        return State.A, ptr + 1
    else:
        tape[ptr] = 0
        return State.D, ptr - 1

# In state D:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state E.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state C.

def stateD(tape, ptr):
    if tape[ptr] == 0:
        tape[ptr] = 1
        return State.E, ptr - 1
    else:
        return State.C, ptr - 1

# In state E:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state F.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.
def stateE(tape, ptr):
    if tape[ptr] == 0:
        tape[ptr] = 1
        return State.F, ptr + 1
    else:
        return State.A, ptr + 1
 
# In state F:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state E.

def stateF(tape, ptr):
    if tape[ptr] == 0:
        tape[ptr] = 1
        return State.A, ptr + 1
    else:
        return State.E, ptr + 1

tape = defaultdict(int)
ptr = 0
state = State.A

handler = {
    State.A: stateA,
    State.B: stateB,
    State.C: stateC,
    State.D: stateD,
    State.E: stateE,
    State.F: stateF
}

for _ in range(12134527):
    state, ptr = handler[state](tape, ptr)

print(sum(tape.values()))