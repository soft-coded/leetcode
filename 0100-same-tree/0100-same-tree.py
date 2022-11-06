# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(n1, n2):
            if not n1 and not n2:
                return True
            if (n1 and not n2) or (n2 and not n1) or n1.val != n2.val:
                return False
            
            left = traverse(n1.left, n2.left)
            right = traverse(n1.right, n2.right)
            
            return left and right
        
        return traverse(p, q)