class Solution:
    def decodeString(self, s: str) -> str:
      stack = []
      num = 0
      cur = ""
      for c in s:
        if c == '[':
          stack.append(cur)
          stack.append(num)
          cur = ""
          num = 0
        elif c == ']':
          curnum = stack.pop()
          prev = stack.pop()
          cur = prev + curnum * cur
        elif c.isdigit():
          num = num * 10 + int(c)
        else:
          cur += c
      return cur