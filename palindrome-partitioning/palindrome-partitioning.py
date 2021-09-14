def isp(st, end, s):
  while st <= end:
    if s[st] != s[end]:
      return False
    st += 1
    end -= 1
  return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
      ans = []
      self.bt(0, ans, [], s)
      return ans
    
    def bt(self, ind, ans, path, s):
      if ind >= len(s): ans.append(path)
      
      for i in range(len(s) - ind):
        if isp(ind, ind + i, s):
          self.bt(ind + i + 1, ans, path + [s[ind:ind+i+1]], s)