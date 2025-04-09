# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         left, right = max(weights), sum(weights)
#         while left < right:
#             mid = (left + right) // 2
#             need=1
#             cur=0

#             for w in weights:
#                 if cur + w > mid:
#                     need += 1
#                     cur = 0
#                 cur += w

#             if need > days: 
#                 left = mid + 1
#             else: 
#                 right = mid

#         return left
class Solution:
    def shipWithinDays(self, W: List[int], days: int) -> int:
        maxW= max(W) 
        l = max(ceil(sum(W)/days), maxW)
        r = min(l + maxW, ceil(len(W) / days) * maxW) # r = l + maxW # also works almost the same. 
        while l < r:
            mid = (l+r)//2 
            curTotal = 0
            daysNeeded = 1 #make sure to initialize to 1 as we are only incrementing daysNeeded when the current load exceeds capacity
            for weight in W:           
                curTotal += weight 
                if curTotal > mid:    #ship current load- wait a day to ship more 
                    curTotal = weight
                    daysNeeded += 1
            if daysNeeded <= days: #capacity is sufficient- see if smaller capacities work
                r = mid
            else: #capacity is too high- reduce search space to higher capacities
                l = mid + 1
        return r