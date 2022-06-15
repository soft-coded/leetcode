# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, arr):
          if not node:
            return
          inorder(node.left, arr)
          arr.append(node.val)
          inorder(node.right, arr)
        
        a1, a2 = [], []
        inorder(root1, a1)
        inorder(root2, a2)
        i = j = 0
        ans = []
        
        while i < len(a1) and j < len(a2):
          if a1[i] < a2[j]:
            ans.append(a1[i])
            i += 1
          else:
            ans.append(a2[j])
            j += 1
        
        while i < len(a1):
          ans.append(a1[i])
          i += 1
          
        while j < len(a2):
          ans.append(a2[j])
          j += 1
        
        return ans
        
        
        
        
        
        