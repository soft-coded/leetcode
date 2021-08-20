class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        ind = []
        s = list(s)
        for i in range(len(s)):
          if s[i] in vows:
            ind.append(i)
        n = len(ind)
        i = 0
        while i < n // 2:
          s[ind[i]], s[ind[n - i - 1]] = s[ind[n - i - 1]], s[ind[i]]
          i += 1
        return ''.join(s)