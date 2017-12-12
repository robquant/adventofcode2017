#cython: boundscheck=False, wraparound=False

from array import array

cdef int solve(jumps, bint part2=False):
    cdef int[:] mem = array('i', jumps)
    cdef int c = 0, ip = 0, n = len(mem), jump = 0
    while 0 <= ip < n:
        jump = mem[ip]
        if part2 and jump >= 3:
            mem[ip] = jump - 1
        else:
            mem[ip] = jump + 1
        ip += jump
        c += 1
    return c

def main():
    jumps = list(map(int, open('december5_input.txt')))
    print(solve(jumps))
    print(solve(jumps, part2=True))
