# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        if not root:
            return res

        q=[]
        q.append(root)

        while q:
            level = []
            size = len(q)
            for i in range(size):
                thisNode = q.pop(0)
                level.append(thisNode.val)
                if thisNode.left:
                    q.append(thisNode.left)
                if thisNode.right:
                    q.append(thisNode.right)
            res.append(sum(level)/size)
        return res
        
        return levels