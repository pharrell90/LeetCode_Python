'''
 A robot is located at the top-left corner of a m x n grid (marked 'Start'
 in the diagram below).

 The robot can only move either down or right at any point in time. The
 robot is trying to reach the bottom-right corner of the grid (marked 'Finish'
 in the diagram below).

 How many possible unique paths are there?

 use dynamic programming to solve problems involved optimization
 like finding maximum or minimum of some values

 runtime: 48ms
'''

class Solution:

    def unique_paths(self, m, n):
        dp = [[1] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    result = s.unique_paths(5, 5)
    print(result)
