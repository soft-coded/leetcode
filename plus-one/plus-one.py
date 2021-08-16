class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        for i in range(len(a)):
          a[i]=str(a[i])
        n = int(''.join(a)) + 1
        return list(str(n))
        