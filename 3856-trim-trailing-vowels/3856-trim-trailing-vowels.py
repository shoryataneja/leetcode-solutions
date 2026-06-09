class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ok = list(s)
        while ok and ok[-1] in 'aeiou':
            ok.pop()
        ans = ""
        for i in ok:
            ans += i 
        return ans