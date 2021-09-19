# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      if not root: return root
      ans = []
      dq = deque()
      dq.append(root)
      while dq:
        l = len(dq)
        for i in range(l):
          node = dq.popleft()
          if i == l - 1:
            ans.append(node.val)
          if node.left: dq.append(node.left)
          if node.right: dq.append(node.right)
      return ans