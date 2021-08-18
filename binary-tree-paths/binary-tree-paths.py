# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
          return [f"{root.val}"]
        ans = []
        def path(node, cur):
          if not node: return
          if not node.left and not node.right:
            ans.append(f"{cur}->{node.val}")
          path(node.left, f"{cur}->{node.val}")
          path(node.right, f"{cur}->{node.val}")
        path(root.left, f"{root.val}")
        path(root.right, f"{root.val}")
        return ans