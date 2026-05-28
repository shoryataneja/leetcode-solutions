class Solution(object):
    def getCommon(self, nums1, nums2):

        s1 = set(nums1)

        for i in nums2:
            if i in s1:
                return i

        return -1