wort = "AAAAAAABCCCCCCDDEEEEE"

def count_chars(wort):
    counter = {}
    for c in wort:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter

class Node:
    def __init__(self, char: str, title: str, count: int, left=None, right=None) -> None:
        self.char = char
        self.title = title
        self.count = count
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.char}: {self.count}"
    
    def show(self):
        print(self.char, self.count)

def huffman(wort):
    nodes = []

    wort_liste = count_chars(wort)
    print("Word list:")
    print(wort_liste)

    # sort ascending
    wort_liste = sorted(wort_liste.items(), key=lambda x: x[1])
    print("Sorted word list:")
    print(wort_liste)

    for char, count in wort_liste:
        nodes.append(Node(char, char, count))

    while len(nodes) > 1:
        right = nodes.pop(0)
        left = nodes.pop(0)
        new_node = Node(None, f"{left.char}-{right.char}", left.count + right.count, left, right)           

        # append new node after right node
        nodes.insert(0, new_node)

        # sort ascending
        nodes = sorted(nodes, key=lambda x: x.count)

    # print all nodes
    codes = {}

    def traverse(node, code):
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(nodes[0], "")

    # order by char
    codes = dict(sorted(codes.items(), key=lambda x: x[0]))
    print("Codes:")
    print(codes)

    # encode
    encoded = ""
    for c in wort:
        encoded += codes[c]

    return encoded

print(huffman(wort))

