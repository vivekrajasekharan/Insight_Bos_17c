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
    from typing import List, Tuple

    class Stack:
        def __init__(self):
            self.data = []  # type: List[Tuple[Node, int]]

        def pop(self) -> 'Tuple[Node, int]':
            return tuple(self.data.pop())

        def push(self, item: 'Tuple[Node, int]'):
            self.data.append(item)

        def __len__(self):
            return len(self.data)
    if node is None:
        return 0
    stk = Stack()
    stk.push((node, 1))
    leaf_depths = []
    while len(stk):
        n, depth = stk.pop()  # type: Node, int
        if n.left is None and n.right is None:
            leaf_depths.append(depth)
        else:
            if n.left is not None:
                stk.push((n.left, depth + 1))
            if n.right is not None:
                stk.push((n.right, depth + 1))
    return max(leaf_depths)


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
