def reverse(st, end, arr):
  while st < end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1

def next_perm(nums):
  n = len(nums)
  i = n - 2
  while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1

  if i >= 0:
    j = n - 1
    while nums[i] >= nums[j]:
      j -= 1

    nums[j], nums[i] = nums[i], nums[j]

  reverse(i + 1, n - 1, nums)

  # return nums 

def factorial(num):
  if num <= 1:
    return 1
  return num * factorial(num - 1)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
      one_less_fac = factorial(n - 1)
      total_perms = 0
      cur_num = 1
      while total_perms < k:
        total_perms += one_less_fac
        cur_num += 1
      
      cur_num -= 1
      total_perms -= one_less_fac
      
      nums = [cur_num]
      for i in range(1, n + 1):
        if i == cur_num:
          continue
        nums.append(i)
      
      k -= total_perms
      
      for i in range(k - 1):
        next_perm(nums)
      return "".join(list(map(str, nums)))
        