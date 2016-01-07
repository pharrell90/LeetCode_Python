'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

runtime: 116ms
'''

class Solution:
    def anagram(self, strs):
        d  = {}
        result = []

        for s in strs:
            t = tuple(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]

        for group in d.vales():
            if len(group) > 1:
                result += group

        return result
