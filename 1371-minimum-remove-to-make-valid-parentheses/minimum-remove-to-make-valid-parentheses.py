class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        stack=[]
        for ch in s:
            if ch=='(':
                left+=1
            elif ch==')':
                right +=1
            if right>left:
                right-=1
            else:
                stack.append(ch)
        result = ""

        while stack:
            current = stack.pop()
            if left>right and current == '(':
                left-=1
            else:
                result+=current
        return result[::-1]
