class Layer():

    def __init__(self, range_):
        self.pos = 1
        self.direction = 1
        self.range_ = range_
        self.empty = (self.range_ == 0)

    def does_catch(self):
        if self.empty:
            return False
        return self.pos == 1

    def step(self, n=1):
        if self.empty:
            return
        n = n % (2 * (self.range_ - 1))
        for i in range(n):
            if self.direction == 1 and self.pos == self.range_:
                self.direction = -1
            elif self.direction == -1 and self.pos == 1:
                self.direction = 1
            self.pos += self.direction

def move_through_layers(layers, delay=0):
    layer_index = -1
    severity = 0
    caught = False
    for layer in layers:
        layer.step(delay)
    while layer_index < len(layers) - 1:
        layer_index += 1
        if layers[layer_index].does_catch():
            print("Delay: {}, caught in layer {}".format(delay, layer_index))
            caught = True
            severity += layer_index * layers[layer_index].range_
        for layer in layers:
            layer.step()
    return caught, severity

def any_lay_at_zero(layers, delay):
    for i, layer in enumerate(layers):
        if layer.range_ == 0:
            continue
        if (delay + i) % (2 * (layer.range_ - 1)) == 0:
            return True
    return False

def gen_layers(input):
    max_index = input[-1][0]
    layers = [Layer(0) for _ in range(max_index + 1)]
    for item in input:
        layers[item[0]] = Layer(item[1])
    return layers

def part1(layers):
    caught, severity = move_through_layers(layers)
    return severity

def part2(input):
    delay = 0
    layers = gen_layers(input)
    while True:
        if delay % 1000000 == 0:
            print(delay)
        if not any_lay_at_zero(layers, delay):
            return delay
        delay += 1

def main():
    input = [line.rstrip('\n').split(":") for line in open("december13_input.txt").readlines()]
    input = [(int(items[0]), int(items[1])) for items in input]
    layers = gen_layers(input)
    print(part1(layers))
    print(part2(input))

def test_part2():
    input = [(0, 3), (1, 2), (4, 4), (6, 4)]
    assert part2(input) == 10

def test_move_through_layers():
    layers = [Layer(0) for _ in range(7)]
    layers[0] = Layer(3)
    layers[1] = Layer(2)
    layers[4] = Layer(4)
    layers[6] = Layer(4)
    _, severity = move_through_layers(layers)
    assert severity == 24

if __name__ == '__main__':
    main()
