class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def formatString(s):
            stack=[]
            for i in range(len(s)):
                if stack and s[i]=='#':
                    stack.pop()
                elif s[i]!='#':
                    stack.append(s[i])
            return stack
        print(formatString(s))
        print(formatString(t))

        return formatString(s)==formatString(t)

