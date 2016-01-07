'''
Given an array of n positive integers and a positive integer s, find the
minimal length of a subarray of which the sum ≥ s. If there isn't one, return
0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

runtime: 48ms
'''

class Solution:
    def minSubArrayLen(self, s, nums):
        Sum = 0
        min_len = len(nums) + 1
        l = []

        for x in nums:
            l.append(x)
            Sum += x
            while Sum >= s:
                Sum -= l.pop(0)
                min_len = min(min_len, len(l) + 1)

        return 0 if min_len > len(nums) else min_len

if __name__ == '__main__':
    s = Solution()
    result = s.minSubArrayLen(7, [2,3,1,1])
    print(result)
