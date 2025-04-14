class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: remove unmatched ')'
        result = []
        open_count = 0
        for c in s:
            if c == '(':
                open_count += 1
                result.append(c)
            elif c == ')':
                if open_count > 0:
                    open_count -= 1
                    result.append(c)
                # else skip it (unmatched ')')
            else:
                result.append(c)

        # Second pass: remove unmatched '(' from the end
        final = []
        open_count = 0
        for c in reversed(result):
            if c == ')':
                open_count += 1
                final.append(c)
            elif c == '(':
                if open_count > 0:
                    open_count -= 1
                    final.append(c)
                # else skip it (unmatched '(')
            else:
                final.append(c)

        return ''.join(reversed(final))

# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         if not s:
#             return True
#         stack = []
#         sl = list(s)
#         for i in range(len(sl)):
#             if sl[i] == "(":
#                 stack.append(i)
#             elif sl[i] == ")":
#                 if stack:
#                     stack.pop()
#                 else:
#                     sl[i] = ""
#         for i in stack:
#             sl[i] = ""
#         return "".join(sl)

