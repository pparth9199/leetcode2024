class Solution:
    def isValid(self, s: str) -> bool:
        checkerDict = {'(':')','{':'}','[':']'}
        cacheStack=[]
        for i in s:
            if i in '{[(':
                cacheStack.append(i)
            elif len(cacheStack)==0 or i!=checkerDict[cacheStack.pop()]:
                return False
        return len(cacheStack)==0

