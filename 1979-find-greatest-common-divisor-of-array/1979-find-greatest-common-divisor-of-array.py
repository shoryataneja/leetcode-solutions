class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ok = sorted(nums)
        mini = ok[0]
        maxi = ok[-1]

        ans = []
        for i in range(1, mini + 1):
            if mini % i == 0 and maxi % i == 0:
                ans.append(i)

        return ans[-1]