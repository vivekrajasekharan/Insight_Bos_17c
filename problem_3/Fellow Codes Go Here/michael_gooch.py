"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node
"""


# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def depth_helper(node):
    # YOUR CODE GOES HERE
    leaf_depth = 0
    if node is None:
        return leaf_depth
    stk = list()
    stk.append((node, 1))
    while len(stk):
        n, depth = stk.pop(0)  # type: Node, int
        print('depth was: ', depth)
        if n.left is None and n.right is None:
            leaf_depth = depth
        else:
            if n.left is not None:
                stk.append((n.left, depth + 1))
            if n.right is not None:
                stk.append((n.right, depth + 1))
    return leaf_depth


# PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
    depth = depth_helper(tree)
    return depth


# test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Depth of tree is %d, and the expected result is 3"
          % (find_max_depth(root),))


if __name__ == "__main__":
    main()
