class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      ans = []
      def inorder(node):
        nonlocal k
        if not node: return
        inorder(node.left)
        ans.append(node.val)
        if len(ans) >= k: return
        inorder(node.right)
      inorder(root)
      return ans[k - 1]