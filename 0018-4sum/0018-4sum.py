class Solution:
    def fourSum(self, nums: List[int], target: int):
        i = 0
        n = len(nums)
        ans = []
        nums.sort()
        
        while i < n:
            j = i + 1
            while j < n:
                tar = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    sumlr = nums[left] + nums[right]
                    if sumlr == tar:
                        ans.append((nums[i], nums[j], nums[left], nums[right]))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    
                    elif sumlr > tar:
                        right -= 1
                    else:
                        left += 1
                
                while j < n - 1 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return ans