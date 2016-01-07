'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.


'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build_tree(self, preorder, inorder):
        self.p = preorder
        self.i = inorder
        return self._dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

    def _dfs(self, l1, r1, l2, r2):
        if l1 > r1: return None
        if l1 == r1: return TreeNode(self.p[l1])

        root = TreeNode(self.p[l1])
        idx = self.i.index(self.p[l1])
        root.left = self._dfs(l1 + 1, l1 + idx - l2, l2, idx - 1)
        root.right = self._dfs(l1 + idx - l2 + 1, r1, idx + 1, r2)

        return root
