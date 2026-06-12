class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0 
        m = 1
        while n != 0 :
            dig = n % 10 
            s += dig 
            m *= dig 
            n = n // 10 

        return m-s
