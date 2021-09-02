class Solution:
    def divide(self, dd: int, ds: int) -> int:
      if dd == -2147483648 and ds == -1:
        return 2147483647
      neg = (dd < 0) ^ (ds < 0)
      dd, ds = abs(dd), abs(ds)
      ans = 0
      while dd >= ds:
        temp, i = ds, 1
        while temp << 1 <= dd:
          temp <<= 1
          i <<= 1
        dd -= temp
        ans += i
      return -ans if neg else ans