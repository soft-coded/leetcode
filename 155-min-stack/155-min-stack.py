class MinStack:

    def __init__(self):
      self.st = []
      self.min_st = []  

    def push(self, val: int) -> None:
      if (self.min_st and val < self.min_st[-1]) or not self.min_st:
        self.min_st.append(val)
      else:
        self.min_st.append(self.min_st[-1])
      self.st.append(val)

    def pop(self) -> None:
      self.min_st.pop()
      self.st.pop()

    def top(self) -> int:
      return self.st[-1]

    def getMin(self) -> int:
      return self.min_st[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()