# DEPTH FIRST SEARCH
# NOTE: DFS can be in 3 ways, Preorder(Iterative DFS), Inorder, Postorder
# where Pre-, In-, Post- represents the place of the Node itself being
# Pre- (node, left, right), In- (left, node, right), Post- (left, right, node)
# every jump you consider whats in the order
# using STACK
# O(H), height, H = n


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


#         1
#     2      3
#   4   5  10
#         11

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)
G = TreeNode(11)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
F.left = G

print("BELOW IS ABOUT PREORDER TRAVERSAL =================================")


# Recursive Pre Order Traversal (DFS)
def display_dfs_preorder(node):
    if not node:
        return
    print(node)
    display_dfs_preorder(node.left)
    display_dfs_preorder(node.right)


print(display_dfs_preorder(A))

print("BELOW IS ABOUT INORDER TRAVERSAL =================================")


def display_dfs_inorder(node):
    if not node:
        return
    display_dfs_inorder(node.left)
    print(node)
    display_dfs_inorder(node.right)


print(display_dfs_inorder(A))

print("BELOW IS ABOUT POSTORDER TRAVERSAL =================================")


def display_dfs_postorder(node):
    if not node:
        return
    display_dfs_postorder(node.left)
    display_dfs_postorder(node.right)
    print(node)


print(display_dfs_postorder(A))

# Below is a trial for  making it inline

print(
    "=================== Below are only representation of Recursive Traversal in Pre Order, In Order, and Post Order using Stack ==================="
)


def dis_pre_order(node):
    preorder = []

    def dfs(node):
        if not node:
            return
        preorder.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(node)
    print("Pre Order Traversal: ", "".join(str(preorder)))


dis_pre_order(A)


def dis_in_order(node):
    inorder = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        inorder.append(node.val)
        dfs(node.right)

    dfs(node)
    print("In Order Traversal: ", "".join(str(inorder)))


dis_in_order(A)


def dis_post_order(node):
    postorder = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        postorder.append(node.val)

    dfs(node)
    print("Post Order Traversal: ", "".join(str(postorder)))


dis_post_order(A)
