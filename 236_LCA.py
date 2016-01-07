# LCA of a binary tree
# If the current (sub)tree contains both p and q, then the function result
# is their LCA. If only one of them is in that subtree, then the result is
# that one of them. If neither are in that subtree, the result is None.
# runtime: 384ms
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowest_common_ancestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowest_common_ancestor(child, p, q) \
                for child in (root.left, root.right))
        return root if left and right else left or right
