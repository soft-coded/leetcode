class Solution:
    def findOcurrences(self, text: str, f: str, s: str) -> List[str]:
      ans = []
      text = text.split()
      for i in range(1, len(text) - 1):
        if text[i] == s and text[i - 1] == f:
          ans.append(text[i + 1])
      return ans