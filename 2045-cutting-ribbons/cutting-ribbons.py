class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total = sum(ribbons)
        if k > total:
            return 0
        
        lo, hi = 1, min(total // k, max(ribbons))
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if sum(x // mid for x in ribbons) >= k:
                lo = mid
            else:
                hi = mid - 1
        
        return lo