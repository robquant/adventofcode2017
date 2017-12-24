import itertools
import time

class Strongest():

    def __init__(self):
        self.max_strength = 0

    def __call__(self, line):
        strength = calc_strength(line)
        if strength > self.max_strength:
            self.max_strength = strength
    
    def __str__(self):
        return "Max strength: %d"%self.max_strength

class StrengthOfLongest():

    def __init__(self):
        self.max_strength = 0
        self.max_length = 0

    def __call__(self, line):
        if len(line) > self.max_length:
            self.max_length = len(line)
            self.max_strength = calc_strength(line)
        elif len(line) == self.max_length:
            if calc_strength(line) > self.max_strength:
                self.max_strength = calc_strength(line)
    
    def __str__(self):
        return "Strength of longest: %d"%self.max_strength

def fits(piece, line):
    return piece[0] == line[-1][1] or piece[1] == line[-1][1]

def calc_strength(line):
    return sum(itertools.chain.from_iterable(line))

def chain(line, available_pieces, reduce_funcs):
    global max_strength
    any_fits = False
    for piece in available_pieces:  
        if fits(piece, line):
            any_fits = True
            line_with_piece = line + [piece] if piece[0] == line[-1][1] else line + [(piece[1], piece[0])]
            available_pieces_less_piece = available_pieces.copy()
            available_pieces_less_piece.remove(piece)
            chain(line_with_piece, available_pieces_less_piece, reduce_funcs)
    if not any_fits:
        for f in reduce_funcs:
            f(line)

start_time = time.time()
start = [(0,0)]
pieces = set((int(line.split('/')[0]), int(line.split('/')[1])) for line in open("december24_input.txt"))
funcs = (Strongest(), StrengthOfLongest())
chain(start, pieces, funcs)
for func in funcs:
    print(func)
print(time.time() - start_time)