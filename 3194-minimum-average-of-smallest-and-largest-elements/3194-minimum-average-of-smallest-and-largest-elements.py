class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        avg = []
        nums.sort()
        for i in range(len(nums)//2):
            ok = (nums[0] + nums[-1]) / 2.0
            avg.append(ok)
            nums.pop(0)
            nums.pop(-1)
        return min(avg)