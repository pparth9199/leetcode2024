class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximumArea = -inf
        l=0
        r=len(height)-1
        while l<r:
            length =  min(height[l],height[r])
            breadth = r-l
            area = length * breadth
            maximumArea = max(maximumArea,area)
            if  height[l]>height[r]:
                r-=1
            else:
                l+=1
        return maximumArea


