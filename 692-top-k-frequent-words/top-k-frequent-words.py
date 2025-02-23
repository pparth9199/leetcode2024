class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs=Counter(words)
        max_heap = []
        for word,freq in freqs.items():
            heapq.heappush(max_heap,(-freq,word)) #maxheap

        result = [heapq.heappop(max_heap)[1] for i in range(k)]
        return result