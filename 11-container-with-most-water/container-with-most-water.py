class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        h = len(height) - 1
        area = 0
        while l<h:
            if height[l] <= height[h]:
                area = max(area, (height[l] * (h-l)))
                l = l + 1
            else:
                area = max(area, (height[h] * (h-l)))
                h = h - 1
        return area