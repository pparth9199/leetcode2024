# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        def dfs(root):
            if not root:
                return None
            heapq.heappush(heap,root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        print(heap)
        for i in range(k):
            ans = heapq.heappop(heap)
        return ans
