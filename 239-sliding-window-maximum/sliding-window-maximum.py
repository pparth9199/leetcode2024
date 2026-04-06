from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()  # This will store indices, not values
        
        for i in range(len(nums)):
            # 1. Remove indices of elements smaller than the current one from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # 2. If the front index is out of the window range, remove it
            if dq[0] == i - k:
                dq.popleft()
            
            # 3. Once we have a full window, the front of dq is our max
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res