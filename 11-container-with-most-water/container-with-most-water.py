class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            if height[l] < height[r]:
                area = max(area, height[l] * (r - l))
                l = l + 1
            else:
                area = max(area, height[r] * (r - l))
                r = r - 1
        return area