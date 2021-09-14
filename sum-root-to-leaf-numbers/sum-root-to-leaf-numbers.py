class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      sm = 0
      def traverse(node, path):
        if node:
          path += str(node.val)
          if not node.left and not node.right:
            nonlocal sm
            sm += int(path)
            return
          traverse(node.left, path)
          traverse(node.right, path)
      traverse(root, "")
      return sm