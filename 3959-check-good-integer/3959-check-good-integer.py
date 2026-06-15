class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digsum = 0
        sqrsum = 0 
        while n != 0:
            dig = n % 10 
            digsum += dig 
            sqrsum += dig * dig 
            n = n // 10
        # return digsum , sqrsum

        if sqrsum - digsum >= 50:
            return True 
        return False 