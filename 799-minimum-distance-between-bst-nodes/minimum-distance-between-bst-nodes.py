# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sortedList = [] 
        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            sortedList.append(root.val)
            dfs(root.right)

            return
        dfs(root)
        ans = float('inf')
        i=0
        j=1
        print(sortedList)
        while j<len(sortedList):
            ans = min(ans,sortedList[j]-sortedList[i])
            i+=1
            j+=1
        return ans


