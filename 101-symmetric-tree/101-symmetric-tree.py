# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(n1, n2):
          if not n1 and not n2:
            return True
          
          if (n1 and not n2) or (n2 and not n1) or n1.val != n2.val:
            return False
          
          if not check(n1.left, n2.right) or not check(n1.right, n2.left):
            return False
          
          return True
        
        return check(root.left, root.right)
            
            
            
            