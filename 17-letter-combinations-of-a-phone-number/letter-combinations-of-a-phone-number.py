class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []

        def backtrack(p, up):
            if len(up) == 0:
                if len(p) == len(digits):
                    return [p]
                return []
            
            result = []
            for ch in pad[up[0]]:
                result += backtrack(p + ch, up[1:])
            
            return result

        words = backtrack("", digits)
        return words
