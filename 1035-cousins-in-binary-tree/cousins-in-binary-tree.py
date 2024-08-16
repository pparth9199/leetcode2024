# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q=deque([root])
        level=0
        while q:
            siblings=False
            cousins=False
            for i in range(len(q)):
                current = q.popleft()
                if not current:
                    siblings = False 
                else:
                    if x==current.val or y==current.val:
                        if not cousins:
                            siblings,cousins = True, True
                        else:

                            return not siblings
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)
                    q.append(None)
            if cousins:
                return False
        return False