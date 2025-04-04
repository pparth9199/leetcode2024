class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        l=0
        while True:
            if i not in arr:
                l+=1
                if l==k:
                    return i
                i+=1
            else:
                i+=1