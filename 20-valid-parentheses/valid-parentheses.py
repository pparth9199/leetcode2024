class Solution:
    def isValid(self, s: str) -> bool:
        checkerDict = {'(':')','{':'}','[':']'}
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif len(stack)==0 or i!=checkerDict[stack.pop()]:
                return False
        return len(stack)==0
