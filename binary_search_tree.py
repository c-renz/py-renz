class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


#         5
#     3      7
#   1   2  6  9
#            8 10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(6)
G = TreeNode(7)
H = TreeNode(8)
I = TreeNode(9)
J = TreeNode(10)

# Left side
E.left = C  # 5 -> 3
E.right = G  # 5 -> 7
C.left = A  # 3 -> 1
C.right = B  # 3 -> 2

# Right side
G.left = F  # 7 -> 6
G.right = I  # 7 -> 9
I.left = H  # 9 -> 8
I.right = J  # 9 -> 10


def binary_search_tree(node, target):
    stk = [node]
    print("node value", node.val)
    print("target: ", target)
    print("============")
    if not node:
        return False
    if node.val == target:
        return print("True")
    if node.val < target:
        binary_search_tree(node.right, target)
    if node.val > target:
        binary_search_tree(node.left, target)


binary_search_tree(E, 10)
