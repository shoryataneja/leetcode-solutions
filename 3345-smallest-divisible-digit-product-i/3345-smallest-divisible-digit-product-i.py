class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        while True:
            ok = n 
            mul = 1 
            while ok != 0:
                dig = ok % 10 
                mul = dig * mul 
                ok = ok // 10 
            # if mul == 0:
            #     return n
            if mul % t == 0:
                return n 
            
            n += 1 
        
    


     
