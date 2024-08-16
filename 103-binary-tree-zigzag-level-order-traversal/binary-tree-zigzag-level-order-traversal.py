# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res

        q=[]
        q.append(root)
        flag=False
        while q:
            level = []
            size = len(q)
            for i in range(size):
                thisNode = q.pop(0)
                
                
                if thisNode.right:
                    q.append(thisNode.right)
                if thisNode.left:
                    q.append(thisNode.left)

                if flag:
                    level.append(thisNode.val)
                else:
                    level.insert(0,thisNode.val)
            flag=not flag        
            res.append(level)
        return res