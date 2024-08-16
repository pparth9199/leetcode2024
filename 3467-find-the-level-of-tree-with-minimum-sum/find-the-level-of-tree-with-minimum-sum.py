# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        minSum=float('inf')
        count=0
        ans=0
        if not root:
            return res

        q=[]
        q.append(root)

        while q:
            count+=1
            currentSum=0
            size = len(q)
            for i in range(size):
                thisNode = q.pop(0)
                currentSum+=thisNode.val
                if thisNode.left:
                    q.append(thisNode.left)
                if thisNode.right:
                    q.append(thisNode.right)
            if currentSum<minSum:
                ans=count
                minSum=currentSum
        return ans