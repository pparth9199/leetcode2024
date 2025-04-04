class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        i = len(heights) - 1 
        lastSeen = heights[i]
        res = [i]
        i-=1

        while i>=0:
            if heights[i] > lastSeen:
                print(heights[i],lastSeen)
                res.append(i)
            lastSeen = max(lastSeen,heights[i])
            i-=1
        

        return res[::-1]
