# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s=="":
            return None
        stack=[]
        sign = 1
        val=0
        i=0
        cur=TreeNode()

        while i <len(s):
            if s[i]=='-':
                sign=-1
            elif s[i].isdigit():
                cur.val = cur.val*10 + sign*int(s[i])
            elif s[i]=='(':
                stack.append(cur)
                cur=TreeNode()
                val = 0
                sign = 1
            elif s[i]==')':
                prev = stack.pop()
                if prev.left==None:
                    prev.left=cur
                else:
                    prev.right=cur
                cur=prev
            i+=1
        return cur