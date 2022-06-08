class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
      c_st = 0
      c_end = len(mat[0]) - 1
      r_st = 0
      r_end = len(mat) - 1
      ans = []
      
      while c_st <= c_end and r_st <= r_end:
        for col in range(c_st, c_end + 1):
          ans.append(mat[r_st][col])
        
        for row in range(r_st + 1, r_end + 1):
          ans.append(mat[row][c_end])
          
        if r_st != r_end:        
          for col in range(c_end - 1, c_st - 1, -1):
            ans.append(mat[r_end][col])
        
        if c_st != c_end:
          for row in range(r_end - 1, r_st, -1):
            ans.append(mat[row][c_st])
        
        r_st += 1
        r_end -= 1
        c_st += 1
        c_end -= 1
      
      return ans