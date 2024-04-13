class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxArea=0
        while l<r:
            length = min(height[l],height[r])
            breadth = r-l
            area = length * breadth
            maxArea = max(maxArea,area)
            if height[l]>=height[r]:
                r-=1
            elif height[r]>height[l]:
                l+=1
        return maxArea