"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                
                for child in thisNode.children:
                    if child:
                        q.append(child)        
            res.append(level)
        return res