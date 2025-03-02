class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap, -i)
        for i in range(k):
            ans = heapq.heappop(heap)
        return -ans