class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
      c = Counter(deck).values()
      return reduce(gcd, c) > 1