class Solution:
    def longestCommonPrefix(self, strs):
        a = strs[0]
        for i in strs:
            while not i.startswith(a):
                a = a[:-1]
        return a