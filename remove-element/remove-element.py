class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = [i for i in nums if i != val]
        k = len(ans)
        for i in range(k):
          nums[i] = ans[i]
        return k