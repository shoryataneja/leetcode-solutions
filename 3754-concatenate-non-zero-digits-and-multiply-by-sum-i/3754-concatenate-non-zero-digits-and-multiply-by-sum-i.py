class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        if n == 0:
            r = 0
        else:
            r = int(str(n).replace("0", ""))
        while n != 0:
            dig = n % 10 
            s = s + dig
            n = n // 10
        return r*s