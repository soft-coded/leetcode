# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
      
      def make_tree(nums, i, j):
        if i > j:
          return None

        mid = (i + j) // 2

        root = TreeNode(nums[mid])
        root.left = make_tree(nums, i, mid - 1)
        root.right = make_tree(nums, mid + 1, j)

        return root
      
      return make_tree(nums, 0, len(nums) - 1)