class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count = Counter(nums)
        for i in count:
            heapq.heappush(heap,(-count[i],i))
        ans=[]
        while k:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans
