class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a=[]
        l=max(candies)
        for i in range (len(candies)):
            if (candies[i]+extraCandies<l):
                a.append(False)
            else:
                a.append(True)
        return a