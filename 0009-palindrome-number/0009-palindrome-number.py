class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        pal = str(x)
        if pal == pal[::-1]:
            return True
        else:
            return False
        