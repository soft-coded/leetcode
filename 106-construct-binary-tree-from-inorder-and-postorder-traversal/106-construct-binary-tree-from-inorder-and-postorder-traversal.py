# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
      inorder_index_map = {}
      for i in range(len(inorder)):
        inorder_index_map[inorder[i]] = i
        
      def make_tree(left, right):
        if left > right: 
          return None
        
        val = postorder.pop()
        root = TreeNode(val)
        
        root.right = make_tree(inorder_index_map[val] + 1, right)
        root.left = make_tree(left, inorder_index_map[val] - 1)
        return root
      
      return make_tree(0, len(postorder) - 1)