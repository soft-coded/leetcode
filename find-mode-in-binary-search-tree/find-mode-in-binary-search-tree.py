# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        def inorder(node):
          if node:
            inorder(node.left)
            d[node.val] = d.get(node.val, 0) + 1
            inorder(node.right)
        inorder(root)
        mx = max(d.values())
        ans = []
        for key, val in d.items():
          if val == mx: ans.append(key)
        return ans