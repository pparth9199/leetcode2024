class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        perms = []

        def backtrack():
            if len(perms) == n:
                res.append(perms[:])
                return
        
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    backtrack()
                    perms.pop()

        backtrack()   
        return res  