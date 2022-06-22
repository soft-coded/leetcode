"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
      if not root: return
      dq = deque()
      dq.append(root)
      while dq:
        n = len(dq)
        for i in range(n):
          node = dq.popleft()
          if i != n - 1:
            node.next = dq[0]
          if node.left:
            dq.append(node.left)
          if node.right:
            dq.append(node.right)
      return root
          
          
          
          
          
          