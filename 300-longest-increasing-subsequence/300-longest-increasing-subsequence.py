class Solution:
  def lengthOfLIS(self, arr: List[int]) -> int:
    ans = []
    for i in range(len(arr)):
      if not ans or arr[i] > ans[-1]:
        ans.append(arr[i])
      else:
        ind = bisect_left(ans, arr[i])
        ans[ind] = arr[i]
    return len(ans)
          