class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c = {')', '}', ']'}
        d = {
          ')': '(',
          '}': '{',
          ']': '['
        }
        for item in s:
          if item in c:
            if len(stack) == 0 or stack[-1] != d[item]:
              return False
            stack.pop()
          else:
            stack.append(item)
        return len(stack) == 0