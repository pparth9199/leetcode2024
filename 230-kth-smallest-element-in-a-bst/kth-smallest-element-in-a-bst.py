# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def dfs(root):
            nonlocal l
            if root:
                l.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        if root == None:
            return None
        dfs(root)
        heapq.heapify(l)
        for i in range(k):
            ans = heapq.heappop(l)
        return ans
