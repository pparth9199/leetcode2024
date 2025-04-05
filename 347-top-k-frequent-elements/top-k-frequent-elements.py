class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        counter = Counter(nums)
        heap = [] 
        
        for i in counter:
            heapq.heappush(heap,(counter[i],i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]


        
        
