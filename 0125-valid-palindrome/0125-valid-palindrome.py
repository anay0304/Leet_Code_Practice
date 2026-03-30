class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        newS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(newS) - 1

        while(l < r):

            if newS[l] != newS[r]:
                return False

            l += 1
            r -= 1

        return True

