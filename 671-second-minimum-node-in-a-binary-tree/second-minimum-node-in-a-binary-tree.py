# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        root_val = root.val
        found = False
        second = inf

        def dfs(root):
            nonlocal root_val,found,second
            if not root:
                return
            if root_val<root.val<second:
                second = root.val
                found=True
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return second if found else -1
            
        # heap = set()
        # def dfs(root):
        #     nonlocal heap
        #     if not root:
        #         return
        #     heap.add(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # print(heap)
        # heap=list(heap)
        # heapq.heapify(heap)
        
        # heapq.heappop(heap)

        # return heapq.heappop(heap) if len(heap)>=1 else -1