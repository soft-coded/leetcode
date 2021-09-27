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