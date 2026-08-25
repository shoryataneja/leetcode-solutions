class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        if k not in nums:
            return k

        # count = 0

        # for i in nums:
        #     if i % k == 0: 
        #         count += 1  
        
        # return (count*k) + k

        m = k 

        for i in nums:
            if i == m :
                m += k 
        
        return m
