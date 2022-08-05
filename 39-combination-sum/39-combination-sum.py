class Solution:
  def combinationSum(self, arr: List[int], k: int):
    ans = []
    n = len(arr)
    def recur(i, cursum, path):
        if cursum == k:
            ans.append(path)
            return
        
        if cursum > k:
            return
        
        for ind in range(i, n):
            if ind > i and arr[ind] == arr[ind - 1]:
                continue
            recur(ind, cursum + arr[ind], path + [arr[ind]])
        
    recur(0, 0, [])
    print(ans)
    return ans
      
      