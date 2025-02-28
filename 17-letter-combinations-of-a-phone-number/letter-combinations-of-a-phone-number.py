class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:['a', 'b' , 'c'], 3:['d','e','f'], 4:['g', 'h', 'i'],
              5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'],
              9:['w','x','y','z']}
        if digits == "":
            return []
        res = []
        n = len(digits)
        stack = [""]
        while stack:
            curr = stack.pop()
            if len(curr) == n:
                res.append(curr)
            else:
                curr_index = len(curr)
                letters = dic[int(digits[curr_index])]
                for l in letters:
                    stack.append(curr + l)
        return res