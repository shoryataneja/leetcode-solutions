class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(num):
            count = 0 
            while num != 0:
                dig = num % 10 
                count += 1 
                num = num // 10
            return count
        ans = 0 
        for i in nums:
            if helper(i) % 2 == 0:
                ans += 1 
        return ans