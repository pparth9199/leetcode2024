class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
        
        while k-1:
            heapq.heappop(heap)
            k-=1
        return -heap[0]