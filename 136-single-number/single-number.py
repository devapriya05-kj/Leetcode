class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
class Solution:
    def singleNumber(self, nums):
        a=0
        for i in nums:
            a=a^i
        return a