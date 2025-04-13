# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def dfs(root):
            nonlocal arr
            if not root:
                return
            dfs(root.left)
            arr.append(root)
            dfs(root.right)
        dfs(root)
        def arrToBST(start,end):
            nonlocal arr
            if start>end:
                return None
            mid = (start+end)//2
            root = arr[mid]
            root.left = arrToBST(start,mid-1)
            root.right = arrToBST(mid+1,end)
            return root
        return arrToBST(0,len(arr)-1)