import heapq

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
    
    def __lt__(self, other):
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count

def huffman(wort):
    nodes = []

    wort_liste = count_chars(wort)
    print("Word list:")
    print(wort_liste)

    for char, count in wort_liste.items():
        heapq.heappush(nodes, Node(char, char, count))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        new_node = Node(None, f"{left.char}-{right.char}", left.count + right.count, left, right)
        heapq.heappush(nodes, new_node)

    # print all nodes
    codes = {}

    def traverse(node, code):
        if node.char:
            codes[node.char] = code
        else:
            traverse(node.left, code + "1") # flip 0 and 1 to flip the tree
            traverse(node.right, code + "0")

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
