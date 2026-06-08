class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        mid = []
        big = []

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                big.append(i)
        return less + mid + big