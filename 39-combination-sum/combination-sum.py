class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                dfs(remaining-candidates[i], combination, i)
                combination.pop()
            
        dfs(target, [], 0)
        return result