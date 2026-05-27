class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            lower = ch
            upper = ch.upper()

            if lower in word and upper in word:
                ans += 1

        return ans