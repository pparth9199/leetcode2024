class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=""
        space_set = set(spaces)
        for i in range(len(s)):
            if i in space_set:
                res+=" "
            res+=s[i]

        return res