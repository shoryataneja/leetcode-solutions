class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ans = 0
        cost.sort(reverse = True)
        if len(cost) <= 2:
            return sum(cost)
        else:
            ans += sum(cost)
            for i in range(2,len(cost),3):
                ans -= cost[i]
        return ans

            