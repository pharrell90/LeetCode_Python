'''
Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit
in the 32-bit signed integer range.

runtime:
'''

class Solution:

    def maximum_gap(self, nums):
        # length = len(nums)
        # if length < 2:
        #     return 0

        # A = min(nums)
        # B = max(nums)
        # bucket_range = max(1, int((B - A - 1) / (length - 1)) + 1)
        # bucket_length = (B - A) / bucket_range + 1
        # buckets = [None] * bucket_length

        # for i in nums:
        #     loc = (i - A) / bucket_range
        #     bucket = buckets[loc]
        #     if bucket is None:
        #         bucket = {'min': i, 'max': i}
        #         buckets[loc] = bucket
        #     else:
        #         bucket['min'] = min(bucket['min'], i)
        #         bucket['max'] = min(bucket['max'], i)

        # max_gap = 0
        # for j in range(bucket_length):
        #     if buckets[j] is None:
        #         continue
        #     k = j + 1
        #     while k < bucket_length and buckets[k] is None:
        #         k += 1
        #     if k < bucket_length:
        #         max_gap = max(max_gap, buckets[k]['min'] - buckets[j]['max'])

        #     j = k

        # return max_gap

        nums.sort()
        max_gap = 0

        for i in range(len(nums) - 1):
            max_gap = max(max_gap, nums[i+1] - nums[i])

        return max_gap


