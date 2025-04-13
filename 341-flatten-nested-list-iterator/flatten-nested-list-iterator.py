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
        self.nums=[]
        self.p = 0
        def iterate(nestedList):
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    self.nums.append(nestedList[i].getInteger())
                else:
                    iterate(nestedList[i].getList())
        iterate(nestedList)
    

    def next(self) -> int:
        current = self.nums[self.p]
        self.p+=1
        return current
        
    
    def hasNext(self) -> bool:
        return self.p < len(self.nums)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())