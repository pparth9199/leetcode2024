# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.p=0
        self.nums=[]
        def iterate(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.nums.append(i.getInteger())
                else:
                    iterate(i.getList())
        iterate(nestedList)
    
    def next(self) -> int:
        nex = self.nums[self.p]
        self.p+=1
        return nex

    def hasNext(self) -> bool:
        return self.p<len(self.nums)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())