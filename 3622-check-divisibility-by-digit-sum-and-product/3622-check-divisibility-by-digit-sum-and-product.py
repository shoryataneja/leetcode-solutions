class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ok = n
        dig_mul = 1 
        dig_sum = 0 
        while n != 0 :
            dig = n % 10 
            dig_mul *= dig
            dig_sum += dig
            n = n // 10 

        if ok % (dig_sum + dig_mul) == 0:
            return True 
        else:
            return False 