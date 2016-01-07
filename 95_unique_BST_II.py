# Unique BST II solved by DFS
# runtime: 108ms

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generate_trees(self, n):
        return self._dfs(1, n)

    def _dfs(self, start ,end):
        if start > end: return [None]
        result = []

        for root_value in range(start, end + 1):
            left_tree = self._dfs(start, root_value - 1)
            right_tree = self._dfs(root_value + 1, end)

            for i in left_tree:
                for j in right_tree:
                    root = TreeNode(root_value)
                    root.left = i
                    root.right = j
                    result.append(root)
        return result

if __name__ == '__main__':
    s = Solution()
    for node in s.generate_trees(5):
        print (node.val, end=' ')
