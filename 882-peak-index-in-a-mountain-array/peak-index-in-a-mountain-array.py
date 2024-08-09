class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0
        l = 0
        r = len(arr)-1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
        
                