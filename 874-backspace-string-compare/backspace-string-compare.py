class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def refineString(s):
            stack=[]
            for i in s:
                if stack and i=='#':
                    stack.pop()
                elif i!='#':
                    stack.append(i)       
            return "".join(stack)
            
        return refineString(s)==refineString(t)