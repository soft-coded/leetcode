def find_common(s1, s2):
  i = 0
  for char in s2:
    if char == s1[i]:
      i += 1
    else:
      break
  return s1[:i]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      shortest = min(strs, key=len)
      for word in strs:
        shortest = find_common(word, shortest)
      return shortest