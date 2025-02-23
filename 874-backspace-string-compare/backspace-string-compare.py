class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i == "#":
                if len(stack1) == 0:
                    continue
                stack1.pop()
            else:
                stack1.append(i)
        for i in t:
            if i == "#":
                if len(stack2) == 0:
                    continue
                stack2.pop()
            else:
                stack2.append(i)
        if stack1 == stack2:
            return True
        else:
            return False