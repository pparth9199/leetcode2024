class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return True
        stack = []
        sl = list(s)
        for i in range(len(sl)):
            if sl[i] == "(":
                stack.append(i)
            elif sl[i] == ")":
                if stack:
                    stack.pop()
                else:
                    sl[i] = ""
        for i in stack:
            sl[i] = ""
        return "".join(sl)

