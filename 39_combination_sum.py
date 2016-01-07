'''
Given a set of candidate numbers (C) and a target number (T), find all unique
combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
1. All numbers (including target) will be positive integers.
2. Elements in a combination (a1, a2, … , ak) must be in non-descending order.
  (ie, a1 ≤ a2 ≤ … ≤ ak).
3. The solution set must not contain duplicate combinations.

runtime: 116ms
'''

class Solution:

    def combination_sum(self, candidates, target):
        candidates.sort()
        self.result = []
        self._dfs(candidates, target, 0, [])

        return self.result

    def _dfs(self, candidates, target, start, value_list):
        length = len(candidates)
        if target == 0 and value_list not in self.result:
            return self.result.append(value_list)

        for i in range(start, length):
            if target < candidates[i]:
                return
            self._dfs(candidates, target - candidates[i],
                      i, value_list + [candidates[i]])

if __name__ == '__main__':
    s = Solution()
    result = s.combination_sum([2,2,4,7,1,9], 13)
    print(result)
