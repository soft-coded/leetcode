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
      self.ans = []
      for item in nestedList:
        self.flatten(item)
      self.ind = 0
      
    def flatten(self, obj):
      if obj.isInteger():
        self.ans.append(obj.getInteger())
        return
      for item in obj.getList():
        self.flatten(item)
      
    def next(self) -> int:
      self.ind += 1
      return self.ans[self.ind - 1]
    
    def hasNext(self) -> bool:
      return self.ind != len(self.ans)