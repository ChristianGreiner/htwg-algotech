wort = "izznti"

def zaehlen(wort):
    counter = {}
    for c in wort:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter

wort_liste = zaehlen(wort)

class Node:
    def __init__(self, char: str, count: int, left=None, right=None) -> None:
        self.char = char
        self.count = count
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.char}: {self.count}"

def huffman(wort_liste):
    nodes = []
    final_nodes = []
    # sort ascending
    wort_liste = sorted(wort_liste.items(), key=lambda x: x[1])
    
    for char, count in wort_liste:
        nodes.append(Node(char, count))
        final_nodes.append(Node(char, count))

    print(nodes)
    
    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = Node(f"{left.char}-{right.char}", left.count + right.count, left, right)

        # append new node after right node
        nodes.insert(0, new_node)
        final_nodes.append(new_node)

        # sort ascending
        nodes = sorted(nodes, key=lambda x: x.count)

    print(final_nodes)


huffman(wort_liste)

