class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
      ans = []
      def inorder(node):
        if node:
          inorder(node.left)
          ans.append(node.val)
          inorder(node.right)
      inorder(root)
      diff = float("inf")
      for i in range(1, len(ans)):
        diff = min(diff, ans[i] - ans[i-1])
      return diff