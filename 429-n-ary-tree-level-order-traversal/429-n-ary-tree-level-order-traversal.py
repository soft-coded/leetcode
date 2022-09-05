"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if not root:
      return []
    dq = deque()
    dq.append(root)
    ans = []
    
    while dq:
      level = []
      for _ in range(len(dq)):
        node = dq.popleft()
        if not node:
          continue
          
        level.append(node.val)
        for child in node.children:
          if not child:
            continue
            
          dq.append(child)
    
      ans.append(level)
    
    return ans
          
      
      
      
      
      
      
      
      
      