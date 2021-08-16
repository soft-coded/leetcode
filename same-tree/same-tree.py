# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1, i1 = [], []
        p2, i2 = [], []
        
        def pre1(node, l):
          if node:
            l.append(node.val)
            pre1(node.left, l)
            pre1(node.right, l)
          else:
            l.append(None)
        def in1(node, l):
          if node:
            in1(node.left, l)
            l.append(node.val)
            in1(node.right, l)
          else:
            l.append(None)
        pre1(p, p1); in1(p, i1)
        pre1(q, p2); in1(q, i2)
        return p1 == p2 and i1 == i2