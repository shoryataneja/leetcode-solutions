class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        lst = list(str(n))
        x = str(x)
        if lst[0] == x:
            return False
        if x in lst:
            return True 
        return False