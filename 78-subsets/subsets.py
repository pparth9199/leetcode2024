
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(p, up):
            res.append(p[:])  # Add the current subset

            for i in range(len(up)):
                ch = up[i]
                p.append(ch)
                backtrack(p, up[i+1:])  # Only move forward
                p.pop()

        backtrack([], nums)
        return res