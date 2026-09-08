class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ok = str(n)
        ok2 = len(ok)
        if ok2 < 4 :
            return 0 
        return abs(n-999)