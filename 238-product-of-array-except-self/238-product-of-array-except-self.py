class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    product = 1
    zeroes = 0
    for num in nums:
      if num == 0:
        zeroes += 1
        continue
      product *= num
    
    if zeroes > 1:
      return [0] * len(nums)
    
    if zeroes == 1:
      ans = []
      
      for num in nums:
        if num == 0:
          ans.append(product)
        else:
          ans.append(0)
      
      return ans
    
    ans = []
    for num in nums:
      ans.append(product // num)
    
    return ans