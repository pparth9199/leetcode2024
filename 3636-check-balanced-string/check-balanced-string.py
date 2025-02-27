class Solution:
    def isBalanced(self, num: str) -> bool:
        se = 0
        so = 0
        for i in range(len(num)):
            if i % 2 == 0:
                se += int(num[i])
            else:
                so += int(num[i])
        return so == se