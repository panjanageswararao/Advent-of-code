import copy


def part1(cups):
    cups = copy.deepcopy(cups)
    current = None
    cups_len = len(cups)

    for i in range(100):
        current_ix = (cups.index(current) + 1) % cups_len if current else 0
        current = cups[current_ix]
        picked_up = []
        for j in range(3):
            picked_up.append(cups[(current_ix + j + 1) % cups_len])
        for p in picked_up:
            cups.remove(p)

        destination = current - 1 or cups_len
        while destination in picked_up:
            destination = destination - 1 or cups_len
        destination_ix = cups.index(destination)

        cups = cups[: destination_ix + 1] + picked_up + cups[destination_ix + 1 :]

    ix_1 = cups.index(1)
    result = cups[ix_1 + 1 :] + cups[:ix_1]
    return "".join(str(i) for i in result)


class Node:
    def __init__(self, value, right=None):
        self.value = value
        self.right = right


def part2(cups):
    cups = copy.deepcopy(cups) + [i for i in range(len(cups) + 1, 1000001)]

    node_map = {}
    prev_node = None
    for cup in cups:
        node = Node(cup)
        node_map[cup] = node
        if prev_node:
            prev_node.right = node
        prev_node = node

    prev_node.right = node_map[cups[0]]

    current = None
    for i in range(10000000):
        current = current.right if current else node_map[cups[0]]
        picked_up = [current.right, current.right.right, current.right.right.right]
        current.right = picked_up[-1].right

        d_value = current.value - 1 or 1000000
        while node_map[d_value] in picked_up:
            d_value = d_value - 1 or 1000000
        destination = node_map[d_value]

        picked_up[-1].right = destination.right
        destination.right = picked_up[0]

    return node_map[1].right.value * node_map[1].right.right.value


with open("input23.txt") as f:
    inputs = [int(i) for i in f.readline()]

    print(part1(inputs))
    print(part2(inputs))
