class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

def insert(node, key, rotations):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key, rotations)
    else:
        node.right = insert(node.right, key, rotations)

    node.height = 1 + max(height(node.left), height(node.right))

    balance = balance_factor(node)

    # Left Left Case
    if balance > 1 and key < node.left.key:
        rotations.append("R")
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
        rotations.append("L")
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
        rotations.append("LR")
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
        rotations.append("RL")
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def get_leaves(node, leaves):
    if node is None:
        return
    if node.left is None and node.right is None:
        leaves.append(str(node.key))
    get_leaves(node.left, leaves)
    get_leaves(node.right, leaves)

# Последовательность чисел
data = [35, 15, 12, 22, 27, 20, 38]
rotations = []
root = None

# Построение дерева с балансировкой
for key in data:
    root = insert(root, key, rotations)

leaves = []
get_leaves(root, leaves)

# Вывод результата
print("".join(leaves), "".join(rotations))
