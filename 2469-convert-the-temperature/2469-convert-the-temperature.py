class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = []
        kel = celsius + 273.15 
        far = (celsius * 1.80) + 32.00 
        ans.append(kel)
        ans.append(far)
        return ans 