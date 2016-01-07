'''
Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

runtime: 48ms
'''
class Solution:

    def combination_sum_3(self, k, n):
        result = []
        def _search_candidate(start, count, sums, nums):
            if count > k or sums > n:
                return
            if count == k and sums == n:
                result.append(nums)
                return
            for x in range(start + 1, 10):
                _search_candidate(x, count + 1, sums + x, nums + [x])

        _search_candidate(0, 0, 0, [])

        return result

if __name__ == '__main__':
    s = Solution()
    result = s.combination_sum_3(3, 9)

    print(result)


