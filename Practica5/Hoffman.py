class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.direction = ''

    def __str__(self):
        return f'{self.symbol} : {self.freq}'


def print_nodes(Node, val=''):
    extra_val = val + str(Node.direction)
    if (Node.left):
        print_nodes(Node.left, extra_val)
    if (Node.right):
        print_nodes(Node.right, extra_val)
    if (not Node.left and not Node.right):
        print(f"{Node.symbol} -> {extra_val}")


chars = ['A', 'E', 'I', 'S', 'T', 'P', '\\n']
freq = [10, 15, 12, 3, 4, 13, 1]
nodes = []
for x in range(len(chars)):
    nodes.append(Node(freq[x], chars[x]))

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda x: x.freq)
    for node in nodes:
        print(node)
    print('----------')
    left = nodes[0]
    right = nodes[1]
    left.direction = 0
    right.direction = 1
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)

print_nodes(nodes[0])
