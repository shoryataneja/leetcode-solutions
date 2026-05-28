class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 2:
            return False
            
        nums.sort()
        m = max(nums)
        if nums[-1] == nums[-2] and len(nums) == m + 1 :
            for i in range(m-1):
                if nums[i] != i+1:
                    return False
            return True 
        else:
            return False