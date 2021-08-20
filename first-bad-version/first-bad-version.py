# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        hi = n
        lo = 0
        while hi >= lo:
          mid = (hi + lo) // 2
          midBad = isBadVersion(mid)
          prevBad = isBadVersion(mid - 1)
          if midBad and not prevBad:
            return mid
          elif midBad and prevBad:
            hi = mid - 1
          elif not midBad and not prevBad:
            lo = mid + 1