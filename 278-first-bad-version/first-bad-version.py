# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n
        while(l<=h):
            if isBadVersion((l+h)//2) == True:
                h = (l+h)//2 - 1
            elif isBadVersion((l+h)//2) != True:
                l = (l+h)//2 + 1
        return l
        