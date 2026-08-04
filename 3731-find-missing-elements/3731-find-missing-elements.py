class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        lar = nums[-1]
        sml = nums[0]
        rng = lar - sml
        ans = []
        for i in range(sml,lar+1):
            if i not in nums:
                ans.append(i)
        # else:
        #     continue 
        return ans