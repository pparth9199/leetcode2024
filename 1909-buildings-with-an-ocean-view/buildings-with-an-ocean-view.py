class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            if heights[res[-1]]<heights[i]:
                res.append(i)
            else:
                continue

        return res[::-1]
            