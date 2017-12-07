from collections import namedtuple

Node = namedtuple("Node", ["name", "weight", "children"])

nodes = {}
weights = {}

def weight(name):
    if name in weights:
        return weights[name]
    node = nodes[name]
    tree_weight = node.weight + sum(weight(n) for n in node.children)
    weights[name] = tree_weight
    return tree_weight

def is_balanced(node):
    return len(node.children) <= 1 or all(weight(child) == weight(node.children[0]) for child in node.children)

def main():
    fathers = set()
    children = set()
    raw = open('december7_input.txt').readlines()
    for line in raw:
        items = line.rstrip('\n').split(' ')
        name = items[0]
        fathers.add(name)
        assert items[1][0] == '('
        assert items[1][-1] == ')'
        node_weight = int(items[1][1:-1])
        node = Node(name, node_weight, [])
        if len(items) > 2:
            for child in items[3:]:
                child = child.rstrip(',')
                children.add(child)
                node.children.append(child)
        nodes[name] = node 
    head = fathers - children
    # This gives us the tree weight for the entirre tree
    for item in head:
        print(item, weight(item))
    for node in nodes.values():
        if not is_balanced(node):
            print(node)
            for child in node.children:
                print("  ", nodes[child], weight(child))

if __name__ == '__main__':
    main()
