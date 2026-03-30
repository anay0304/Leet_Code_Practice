class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numSet = set(nums)
        maxL = 0

        for i in numSet:

            if i - 1 not in numSet:
                length = 0

                while (i + length) in numSet:
                    length += 1

                maxL = max(length, maxL)
        return maxL