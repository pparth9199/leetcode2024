# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res=[]
        def dfs(root):
            if not root:
                return 
            
            dfs(root.right)
            self.res.append(root.val)
            dfs(root.left)
        dfs(root)
        

    def next(self) -> int:
        return self.res.pop()
    def hasNext(self) -> bool:
        return len(self.res)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()