
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.data, end="")
        inorder_traversal(node.right)

# Список чисел
data = [12,8,16,14,10,4,2,6,5]

# Создание корня дерева
root = Node(data[0])

# Добавление остальных элементов в дерево
for i in range(1, len(data)):
    insert(root, data[i])

# Обход дерева в порядке "левое поддерево - корень - правое поддерево"
inorder_traversal(root)
