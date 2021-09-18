# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(node, ans):
  if node:
    inorder(node.left, ans)
    ans.append(node.val)
    inorder(node.right, ans)
    
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
      self.ind = 0
      self.inorder = []
      inorder(root, self.inorder)

    def next(self) -> int:
      self.ind += 1
      return self.inorder[self.ind - 1]

    def hasNext(self) -> bool:
      return self.ind != len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()