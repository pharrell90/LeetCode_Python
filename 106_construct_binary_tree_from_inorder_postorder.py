'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

runtime: 104ms
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:

#     def build_tree(self, inorder, postorder):
#         return self._new_tree(inorder, postorder)

#     def _new_tree(self, inorder, postorder):
#         if len(postorder) == 0:
#             return None

#         root = TreeNode(postorder[-1])
#         idx = inorder.index(postorder[-1])
#         right_size = len(inorder[idx+1:])
#         left_size = len(inorder) - right_size - 1

#         if right_size > 0:
#             root.right = self._new_tree(inorder[idx+1:],
#                             postorder[-len(right_size+1): -1])
#         if left_size > 0:
#             root.left = self._new_tree(inorder[:idx],
#                             postorder[:left_size])
#         return root

class Solution:

    def build_tree(self, inorder, postorder):
        if not inorder: return None
        self.inorder = inorder
        self.postorder = postorder

        return self._dfs(0, 0, len(inorder))

    def _dfs(self, in_left, post_left, length):
        if length <= 0: return None
        root = TreeNode(self.postorder[post_left + length - 1])
        root_idx = self.inorder.index(self.postorder[post_left +
                         length - 1])
        root.left = self._dfs(in_left, post_left, root_idx - in_left)
        root.right = self._dfs(root_idx + 1, post_left + root_idx -
                        in_left, length - (root_idx - in_left) - 1)
        return root
