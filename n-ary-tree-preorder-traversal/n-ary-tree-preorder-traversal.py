"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
      st = [root]
      ans = []
      while st:
        node = st.pop()
        if node:
          ans.append(node.val)
          st.extend(node.children[::-1])
      return ans