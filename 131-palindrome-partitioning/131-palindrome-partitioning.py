def is_palin(st, end, s):
  while st < end:
    if s[st] != s[end]:
      return False
    st += 1
    end -= 1
  return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
      ans = []
      
      def bt(ind, ans, path, s):
        if ind >= len(s): 
          ans.append(path)

        for i in range(len(s) - ind):
          if is_palin(ind, ind + i, s):
            end = ind + i + 1
            sub_s = s[ind:end]
            bt(end, ans, path + [sub_s], s)
            
      bt(0, ans, [], s)
      return ans
    
