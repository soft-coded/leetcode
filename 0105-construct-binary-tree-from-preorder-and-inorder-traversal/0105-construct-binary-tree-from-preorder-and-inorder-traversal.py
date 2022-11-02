# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        in_map = {}
        
        for i, val in enumerate(inorder):
            in_map[val] = i
        
        pre_ind = 0
        def make_tree(left, right):
            if left > right:
                return None
            
            nonlocal pre_ind
            root_val = preorder[pre_ind]
            root_ind = in_map[root_val]
            root = TreeNode(root_val)
            pre_ind += 1
            
            root.left = make_tree(left, root_ind - 1)
            root.right = make_tree(root_ind + 1, right)
            
            return root        
        
        return make_tree(0, len(inorder) - 1)