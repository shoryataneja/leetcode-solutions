class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        ok = sorted(capacity)
        ok.sort()
        ans = 0
        for i in range (len(capacity)) :
            if ok[i] == itemSize:
                ans = ok[i] 
                break
            elif ok[i] > itemSize:
                ans = ok[i]
                break
        # return capacity
        if ans > 0 :
            return capacity.index(ans)
        else:
            return -1 
        