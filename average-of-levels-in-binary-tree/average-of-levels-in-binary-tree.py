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
      sm = 0
      while dq:
        l = len(dq)
        for i in range(l):
          node = dq.popleft()
          sm += node.val
          if node.left:
            dq.append(node.left)
          if node.right:  
            dq.append(node.right)
        ans.append(sm / l)
        sm = 0
      return ans