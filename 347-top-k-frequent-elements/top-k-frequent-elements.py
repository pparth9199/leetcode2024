class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = collections.Counter(nums)
        # Use heapq.nlargest() to find the k most frequent elements
        top_k_frequent = heapq.nlargest(k, frequency_map.keys(), key=frequency_map.get)
        return top_k_frequent