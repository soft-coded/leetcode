# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    dq = deque()
    dq.append(root)
    level = 1
    mx = -inf
    ans = 1
    while dq:
      sm = 0
      for _ in range(len(dq)):
        node = dq.popleft()
        sm += node.val
        if node.left:
          dq.append(node.left)
        if node.right:
          dq.append(node.right)
      if sm > mx:
        mx = sm
        ans = level
      level += 1
    return ans
      