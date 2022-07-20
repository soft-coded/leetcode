# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, k: int):
    parents = {}
    dq = deque()
    dq.append(root)
    parents[root.val] = None
    ans = []
    while dq:
      for _ in range(len(dq)):
        node = dq.popleft()
        if node.left:
          parents[node.left.val] = node
          dq.append(node.left)
        if node.right:
          parents[node.right.val] = node
          dq.append(node.right)
    
    dq.append(target)
    cur_level = 0
    visited = set()
    while cur_level < k:
      for _ in range(len(dq)):
        node = dq.popleft()
        visited.add(node.val)
        if parents[node.val] and parents[node.val].val not in visited:
          dq.append(parents[node.val])
        if node.left and node.left.val not in visited:
          dq.append(node.left)
        if node.right and node.right.val not in visited:
          dq.append(node.right)
      cur_level += 1
      
    while dq:
      ans.append(dq.popleft().val)
    return ans
    