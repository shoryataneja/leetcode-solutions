class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        if m == 1:
            return ["." * n]

        if n == 1:
            return ["."] * m

        grid = ["." * n]

        for _ in range(m - 1):
            grid.append("#" * (n - 1) + ".")

        return grid