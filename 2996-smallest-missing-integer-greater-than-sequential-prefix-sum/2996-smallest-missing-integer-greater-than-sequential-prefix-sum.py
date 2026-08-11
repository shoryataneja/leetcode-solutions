class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        p = [0]*n
        p[0] = nums[0]

        for i in range(1,n):
            p[i] = p[i-1] +nums[i]

        idx = 0 
        
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                idx += 1 
            else:
                break 
        
        s = p[idx]

        nums_set = set(nums)

        while s in nums_set:
            s += 1 
        return s
