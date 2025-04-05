class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        counter = {}

        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i] = 1

        heap = [] 
        for i in counter:
            heapq.heappush(heap,(counter[i],i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]


        
        
