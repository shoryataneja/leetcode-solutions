class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowels = "aeiouAEIOU"
        has_vowel = False
        has_consonant = False

        for ch in word:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

            elif '0' <= ch <= '9':
                continue

            else:
                return False

        if has_vowel and has_consonant:
            return True
        else:
            return False