'''
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

use dp to determine the maximum profit

runtime: 52ms
'''

class Solution:

    def rob(self, nums):
        if not nums: return 0
        length = len(nums)
        dp = [0] * (length + 1)
        dp[0], dp[1] = 0, nums[0]

        for i in range(2, length + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[length]

if __name__ == '__main__':
    s = Solution()
    result = s.rob([20,50, 900, 1000, 200, 400, 0])
    print(result)
