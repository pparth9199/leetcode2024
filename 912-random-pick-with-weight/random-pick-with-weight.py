class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total_sum = sum(w)
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight / total_sum  # Store cumulative probability
            self.prefix_sums.append(prefix_sum)

        

    def pickIndex(self) -> int:
        target = random.random()    # Generate a number in [0,1)
        
        l , h = 0 , len(self.prefix_sums) - 1
        while l < h:
            mid = (l + h) // 2
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                h = mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()