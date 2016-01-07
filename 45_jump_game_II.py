'''
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

runtime:
'''

class Solution:

    def jump(slef, nums):
        # n = len(nums)
        # start, end, step = 0, 0, 0
        # while end < n - 1:
        #     step += 1
        #     max_end = end + 1
        #     for i in range(start, end + 1):
        #         if i + nums[i] >= n - 1:
        #             return step
        #         max_end = max(max_end, i + nums[i])
        #     start, end = end + 1, max_end

        # return step

        max_reach, next_max_reach, step = 0, 0, 0
        for i in range(len(nums) - 1):
            next_max_reach = max(next_max_reach, i + nums[i])
            if i == max_reach:
                step, max_reach = step + 1, next_max_reach
        return step
