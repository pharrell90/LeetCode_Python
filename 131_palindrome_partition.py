# palindrome partitioning using DFS

class Solution:
    def partition(self, s):
        self.result = []
        self._dfs(s, [])
        return self.result

    def _dfs(self, s, res):
        if not s:
            self.result.append(res)
            return
        for i in range(1, len(s) + 1):
            word = s[:i]
            if word == word[::-1]:
                self._dfs(s[i:], res + [word])

if __name__ == '__main__':
    s = Solution()
    print(s.partition('abbaa'))


