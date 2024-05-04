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

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return count_leaves(node.left) + count_leaves(node.right)

# Список чисел
data = [12,8,16,14,10,4,2,6,5]

# Создание корня дерева
root = Node(data[0])

# Добавление остальных элементов в дерево
for i in range(1, len(data)):
    insert(root, data[i])

# Подсчёт листьев
num_leaves = count_leaves(root)

# Вывод результата
print("Количество листьев:", num_leaves)
