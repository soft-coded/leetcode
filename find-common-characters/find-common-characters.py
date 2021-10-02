class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
      for i in range(len(words)):
        a = [0] * 26
        for item in words[i]:
          a[ord(item) - ord('a')] += 1
        words[i] = a
      ans = []
      for i in range(26):
        low = math.inf
        for item in words:
          if not item[i]:
            low = 0
            break
          low = min(low, item[i])
        ans.extend([chr(ord('a') + i)] * low)
      return ans