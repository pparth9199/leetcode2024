class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sl = path.split("/")
        for i in range(len(sl)):
            if sl[i] == "." or sl[i]=="":
                continue
            elif sl[i]=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(sl[i])
        return "/"+"/".join(stack)
