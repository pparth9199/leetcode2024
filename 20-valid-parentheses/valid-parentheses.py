class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif i == "]":
                if not stack or stack.pop() != "[":
                    return False
        if len(stack) != 0:
            return False
        return True
