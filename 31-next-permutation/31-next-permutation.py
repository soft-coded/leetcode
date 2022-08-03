def reverse(arr, st, end):
    while st < end:
        arr[st], arr[end] = arr[end], arr[st]
        st += 1
        end -= 1

class Solution:
  def nextPermutation(self, perm: List[int]) -> None:
    n = len(perm)
    i = n - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
      i -= 1
    
    if i >= 0:
      j = i + 1
      while j < n and perm[j] > perm[i]:
        j += 1
      j -= 1
      perm[i], perm[j] = perm[j], perm[i]
    
    reverse(perm, i + 1, n - 1)
    return perm