# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_map = {}
        
        for i, val in enumerate(inorder):
            in_map[val] = i
        
        def make_tree(left, right):
            if left > right:
                return None
            
            root_val = postorder.pop()
            root_ind = in_map[root_val]
            root = TreeNode(root_val)
            
            root.right = make_tree(root_ind + 1, right)
            root.left = make_tree(left, root_ind - 1)
            
            return root        
        
        return make_tree(0, len(inorder) - 1)