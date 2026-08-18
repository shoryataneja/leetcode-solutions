class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}

        for i in range(len(nums) - k + 1):
            subarray = nums[i:i+k]
            seen = set(subarray)

            for x in seen:
                count[x] = count.get(x, 0) + 1

        answer = -1

        for x in count:
            if count[x] == 1:
                answer = max(answer, x)

        return answer
        