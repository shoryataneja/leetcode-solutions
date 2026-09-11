class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0 :
                continue 

            for j in range(n):
                if j == i :
                    continue 
                
                for k in range(n): 
                    if k == j or k == i :
                        continue 
                    
                    if digits[k] % 2 == 0:
                        ok = digits[i] * 100 + digits[j] * 10 + digits[k]

                        ans.add(ok)
        return len(ans)