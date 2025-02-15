class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        if len(prices) == 1:
            return 0
        b = 0
        s = 1
        while(1):
            if prices[s] > prices[b]:
                if prices[s] - prices[b] > max:
                    max = prices[s] - prices[b]
            else:
                b = s
            if s == len(prices)-1:
                break
            s = s + 1
        return max