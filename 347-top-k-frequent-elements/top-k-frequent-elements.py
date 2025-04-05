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
            heapq.heappush(heap,(-counter[i],i))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        
        
