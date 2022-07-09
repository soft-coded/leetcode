# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_tree(inorder, preorder):
  pre_ind = 0
  in_map = {}
  for ind, val in enumerate(inorder):
    in_map[val] = ind
    
  def make_tree(left, right):
    if left > right:
      return None
    
    nonlocal pre_ind
    node_val = preorder[pre_ind]
    pre_ind += 1
    node = TreeNode(node_val)
    
    node.left = make_tree(left, in_map[node_val] - 1)
    node.right = make_tree(in_map[node_val] + 1, right)
    
    return node
  
  return make_tree(0, len(inorder) - 1)


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
      inorder = sorted(preorder)
      return get_tree(inorder, preorder)