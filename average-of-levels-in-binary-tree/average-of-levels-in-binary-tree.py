# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
      dq = deque()
      dq.append(root)
      ans = []
      while dq:
        sm = 0; n = 0
        level = deque()
        while dq:
          node = dq.popleft()
          sm += node.val
          n += 1
          if node.left:
            level.append(node.left)
          if node.right:  
            level.append(node.right)
        dq = level
        ans.append(sm / n)
      return ans