class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic= collections.Counter(nums)
        dic={k: v for k, v in sorted(dic.items(), key=lambda item: -item[1])}
        return list(dic.keys())[:k]
