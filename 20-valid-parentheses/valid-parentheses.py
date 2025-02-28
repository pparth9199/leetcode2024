class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '{':'}','[':']'}
        stack =[]
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] in dic:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if s[i] != dic[bracket]:
                    return False
        if stack:
            return False
        return True