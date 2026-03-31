class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        sSet = set()
        l = 0
        maxL = 0

        for r in range(len(s)):
            while s[r] in sSet:
                sSet.remove(s[l])
                l += 1

            sSet.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL