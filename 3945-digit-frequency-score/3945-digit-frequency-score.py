class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        ok = list(str(n))
        freq = {}
        for i in ok:
            if i in freq:
                freq[i] += 1 
            else:
                freq[i] = 1 
        ans = 0
        for i,j in freq.items():
            ans += int(i)*int(j) 
        return ans
