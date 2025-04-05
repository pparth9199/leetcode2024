class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        res=""

        for i in s:
            if not stack:
                stack.append(i)
            elif i != stack[-1]:
                stack.append(i)
                
            else:
                if stack: stack.pop()
        return "".join(stack)
            