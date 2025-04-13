# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l=0
        r=len(nums)-1
        
        def construct(start,end):
            if start>end:
                return
            mid=(start+end)//2
            root = TreeNode(nums[mid])
            root.left = construct(start,mid-1)
            root.right = construct(mid+1,end)
            return root
        return construct(l,r)

            