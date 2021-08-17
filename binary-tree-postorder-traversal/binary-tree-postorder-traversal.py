class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post = []
        def postorder(node):
          if node:
            postorder(node.left)
            postorder(node.right)
            post.append(node.val)
        postorder(root)
        return post