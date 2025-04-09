# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=0,n

        while l<=r:
            mid = (l+r)//2
            isBad = isBadVersion(mid)
            if isBad:
                if mid>0 and isBadVersion(mid-1):
                    r=mid-1
                else:
                    return mid
            else:
                l=mid+1

        