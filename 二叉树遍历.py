class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def layer_traverse(tree):
    stack = [tree]
    while stack:
        current = stack.pop(0)
        print(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)



def deep_traverse(tree):
    if not tree:
        return
    print(tree.data)
    deep_traverse(tree.left)
    deep_traverse(tree.right)


def depth(tree):
    if not tree:
        return 0
    return max(depth(tree.left), depth(tree.right)) + 1


def is_same_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif tree1 and tree2:
        return tree1.data == tree2.data and is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)
    else:
        return False

if __name__ == '__main__':
    tree = Node(1, Node(2, Node(3, Node(4, Node(5), Node(6)))), Node(12, Node(13, Node(14, Node(15), Node(16)))))
    tree2 = Node(1, Node(9, Node(3, Node(4, Node(5), Node(6)))), Node(12, Node(13, Node(14, Node(15), Node(16)))))

    # deep_traverse(tree)
    # layer_traverse(tree)
    print(is_same_tree(tree2, tree))