# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def is_leaf(node):
  if node and not node.left and not node.right:
    return True
  return False

class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    ans = []
    
    def traverse(node, path):
      if not node:
        return
      
      new_path = path + f"->{node.val}"
      if is_leaf(node):
        ans.append(new_path[2:])
        return
      
      traverse(node.left, new_path)
      traverse(node.right, new_path)
      
    traverse(root, "")
    return ans
      
      
      
      
      
      
      
      