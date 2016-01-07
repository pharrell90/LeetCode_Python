'''
 Given an array of non-negative integers, you are initially positioned at the
 first index of the array.

 Each element in the array represents your maximum jump length at that position.

 Determine if you are able to reach the last index.

 For example:
 A = [2,3,1,1,4], return true.

 A = [3,2,1,0,4], return false.

 at each position, you can jump at least one step in order to move
 towards the end. If the maximum you can jump is 0, then you can't reach
 the end position

 runtime: 60ms
'''

class Solution:

    def can_jump(self, nums):
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    result = s.can_jump([2,3,1,0,1,4])
    print(result)
