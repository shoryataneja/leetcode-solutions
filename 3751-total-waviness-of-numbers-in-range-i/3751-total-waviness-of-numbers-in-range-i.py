class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # s = str(num1)
        def helper(num):
            s = str(num)
            ans = 0
            if len(s) < 3:
                return 0
            for i in range(1,len(s)-1):
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    ans += 1 
                if s[i] < s[i-1] and s[i] < s[i+1]:
                    ans += 1
            return ans
            
        ok = 0 

        for i in range(num1,num2+1):
            ok += helper(i)
        return ok