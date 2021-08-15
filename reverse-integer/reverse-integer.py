class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(x))
        if l[0] == '-':
          l = ['-'] + l[len(l) - 1:0:-1]
        else:
          l.reverse()
        l = int(''.join(l))
        return l if -2**31 < l < 2**31 - 1 else 0