class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        
        def make_tree(pre_s, pre_e, in_s, in_e):
          if pre_s > pre_e or in_s > in_e:
            return None
          
          node = TreeNode(preorder[pre_s])
          in_index = inorder_index_map[node.val]
          nums_left = in_index - in_s
          
          node.left = make_tree(pre_s + 1, pre_s + nums_left, in_s, in_index - 1)
          node.right = make_tree(pre_s + nums_left + 1, pre_e, in_index + 1, in_e)
          
          return node
        
        return make_tree(0, len(preorder) - 1, 0, len(inorder) - 1)
          