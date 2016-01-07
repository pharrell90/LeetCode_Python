'''
 Given a binary tree and a sum, determine if the tree has a root-to-leaf path
 such that adding up all the values along the path equals the given sum.

 runtime: 100ms
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def has_path_sum(self, root, sum):
        if not root:
            return False
        if not (root.left or root.right):
            return root.val == sum
        return self.has_path_sum(root.left, sum - root.val) or \
            self.has_path_sum(root.right, sum - root.val)

if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(11)
    node4 = TreeNode(13)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(5)
    node9 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9

    s = Solution()
    result = s.has_path_sum(root, 22)
    print(result)
