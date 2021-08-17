# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sm: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return root.val == sm
        
        return (self.hasPathSum(root.left, sm - root.val)) or self.hasPathSum(root.right, sm - root.val)