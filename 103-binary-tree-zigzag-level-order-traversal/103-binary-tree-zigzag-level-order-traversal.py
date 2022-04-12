# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root: return []
      ans = []
      dq = deque()
      dq.append(root)
      ltr = True
      while dq:
        vals = []
        for i in range(len(dq)):
          node = dq.popleft()
          vals.append(node.val)
          if node.left: dq.append(node.left)
          if node.right: dq.append(node.right)
        if not ltr:
          vals.reverse()
        ans.append(vals)
        ltr = not ltr
      return ans

          