class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ok = len(flowerbed)
        if n == 0:
            return True
        zero = 0 
        for i in range(ok):
            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (i == ok - 1 or flowerbed[i + 1] == 0)
                if left and right:
                    flowerbed[i] = 1
                    zero += 1

                    if zero >= n:
                        return True
        return False