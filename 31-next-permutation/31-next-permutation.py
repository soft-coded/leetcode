class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def check(s, m):
            z = 0
            if s != sorted(s, reverse = True):
                return False
            else:
                for x in range(len(s) - 1, -1, -1):
                    if s[x] > m:
                        return x + 1
        temp = 0
        c = 1
        for x in range(len(nums) - 2, -1, -1):
            if nums[x] >= nums[x + 1]:
                c = c + 1
                continue
            else:
                z = check(nums[x + 1:], nums[x])
                if z != False and x >= 0:
                    temp = nums[x]
                    nums[x] = nums[x + z]
                    nums[x + z] = temp
                nums[x + 1:] = nums[x + 1:][::-1]
                break
        if c == len(nums) :            
            start = 0            
            end = len(nums) - 1            
            while start<end:                
                temp = nums[start]                
                nums[start] = nums[end]                
                nums[end]=temp                
                start+=1                
                end-=1