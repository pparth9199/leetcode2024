class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(p, up):
            if len(up) == 0:
                return [p]  # Return a list containing the current permutation
            ans = []
            ch = up[0]
            for i in range(len(p) + 1):  # Adjusted the loop to allow ch to be inserted at the end
                first = p[:i]
                second = p[i:]
                ans.extend(perm(first + [ch] + second, up[1:]))  # Concatenate lists properly
            return ans

        return perm([], nums)