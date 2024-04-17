class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = collections.Counter(nums)
        heap = []
        
        # Push elements into the heap
        for num, freq in frequency_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
        
        # Extract the top k frequent elements from the heap
        top_k_frequent = [elem[1] for elem in heap]
        
        return top_k_frequent