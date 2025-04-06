class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = defaultdict(list)

        for i,v in enumerate(nums):
            if v in cache:
                for j in cache[v]:
                    res = abs(i-j)
                    if res<=k:
                        return True
            cache[v].append(i)
        return False
        