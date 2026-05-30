class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0 
        for i in range(n):
            if nums[i] == 0 :
                count += 1 
        ok = 0
        for i in range(n-1,n - count-1,-1):
            if nums[i] == 0:
                ok += 1 
        return count - ok 

        