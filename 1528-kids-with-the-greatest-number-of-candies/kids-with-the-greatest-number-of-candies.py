class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tf=[False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                tf[i]=True

        return tf