# class Solution:
  # def canPartitionKSubsets(self, a: List[int], k: int):
#     sm = sum(a)
#     if sm % k:
#       return False
    
#     a.sort(reverse=True)
#     target = sm // k
#     used = [False] * len(a)
#     memo = {}
    
#     def bt(i, k, cursum):
#       if k == 0:
#         return True
#       if cursum == target:
#         return bt(0, k - 1, 0)

#       for j in range(i, len(a)):
#         if used[j] or cursum + a[j] > target:
#           continue
#         used[j] = True
#         if bt(i + 1, k, cursum + a[j]):
#           return True
#         used[j] = False
      
#       return False

#     return bt(0, k, 0)


class Solution:
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    
    if k > len(nums):
        return False
    
    if sum(nums) % k != 0:
        return False
    
    target = sum(nums) / k
    memo = {}
    used = 0


    def backtrack(k, currPath, nums, start, used, target):

        # if no more bucket left, return True. Since each bucket sum == target, that times k, equals array sum.
        if k == 0:

            return True

        # if bucket sum == target, recursively fill the next bucket. 
        if sum(currPath) == target:

            #choose element from nums[0]
            res = backtrack(k-1, [], nums, 0, used, target)
            
            #record the result into memo
            memo[used] = res
            return res

        #if current state had happened before, return its result.
        if used in memo:
            return memo[used]

        #for each bucket, search entire array to find element to fill in the bucket
        for i in range(start, len(nums)):

            #if nums[i] had been chosed, continue
            if (used >> i ) & 1 == 1:
                continue 

            # if the bucket can not fill nums[i], continue
            if nums[i] + sum(currPath) > target:
                continue 

            #otherwise, fill the bucket with nums[i]
            used |= (1 << i) 

            currPath.append(nums[i])
            
            # and check if the next element can be filled in the same bucket. 
            if backtrack(k, currPath , nums, i + 1, used, target):
                return True 

            used ^= (1 << i)

            currPath.pop()
        
        return False 

    
    return backtrack(k, [] ,nums,0,used,target)