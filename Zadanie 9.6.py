class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)



def count_leafs(top):
    i=0
    if top is None:
        return
    stack = list()   # stos symulujemy przez listę Pythona
    stack.append(top)
    while stack:
        node = stack.pop()
        if (node.right==None and node.left==None):
            i=i+1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return i

def count_total(top):
    i=0
    if top is None:
        return
    stack = list()   # stos symulujemy przez listę Pythona
    stack.append(top)
    while stack:
        node = stack.pop()
        i=i+node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return i

print(count_leafs(root))

print(count_total(root))

