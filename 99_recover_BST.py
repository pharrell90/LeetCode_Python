'''
Two elements of a binary search tree (BsT) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise
a constant space solution?

runtime:
'''

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

# class Solution:

#     def recover_tree(self, root):
#         l = []
#         lp = []
#         self._inorder(root, l, p)
#         l.sort()

#         for i in range(len(l)):
#             lp[i].val = l[i]

#         return root

#     def _inorder(self, root, l, lp):
#         if root:
#             self._inorder(root.left, l, lp)
#             l.append(root.val)
#             lp.append(root)
#             self._inorder(root.right, l, lp)

class Solution:

    def recover_tree(self, root):
        self.node1 = None
        self.node2 = None
        self.prev = None
        self._find_two_nodes(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        return root

    def _find_two_nodes(self, root):
        if root:
            self._find_two_nodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.node2 = root
                if not self.node1:
                    self.node1 = self.prev
            self.prev = root
            self._find_two_nodes(root.right)
