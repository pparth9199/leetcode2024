class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        if len(arr)<3:
            return max(arr)
        while l<=r:
            mid = (l+r)//2

            if mid>0 and mid <len(arr):
                if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                    return mid
            if mid<len(arr) and arr[mid+1]<arr[mid]:
                r=mid-1
            else:
                l=mid+1