class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subHelper(p,up):
            if len(up)==0:
                return [p]

            ch = up[0]
            ans = []

            left = subHelper(p+[ch],up[1:])
            right = subHelper(p,up[1:])

            ans.extend(left+right)

            return ans

        return subHelper([],nums)