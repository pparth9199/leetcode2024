# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if root==None:
            return res
        
        queue=[]
        queue.append(root)

        while queue:
            currentNode=[]
            currentSize = len(queue)
            for i in range(currentSize):
                thisNode = queue.pop(0)
                currentNode.append(thisNode.val)
                if thisNode.left!=None:
                    queue.append(thisNode.left)
                if thisNode.right!=None:
                    queue.append(thisNode.right)
            res.append(currentNode)

        return res