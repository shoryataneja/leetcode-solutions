class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            lower = ch 
            upper = ch.upper()

            if lower in word and upper in word:
                lower_i = -1 
                upper_i = -1 

                for i in range(len(word)-1,-1,-1):
                    if word[i] == lower:
                        lower_i = i 
                        break 
                
                for i in range(len(word)):
                    if word[i] == upper:
                        upper_i = i 
                        break 

                if lower_i < upper_i:
                    count += 1 
        return count 
