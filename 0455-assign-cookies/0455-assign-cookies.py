class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        n = len(g) #length of greed factor array 
        m = len(s) #lenght of cookie size array
        l = 0 #pointer for cookie
        r = 0 #pointer for greed

        while (l < m and r < n):
            if g[r] <= s[l]:
                r += 1 
            l += 1 
        return r
        