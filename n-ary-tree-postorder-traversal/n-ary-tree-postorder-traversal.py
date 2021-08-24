"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
      ans = []
      def po(node):
        if not node: return
        i = 0
        while i < len(node.children):
          po(node.children[i])
          i += 1
        ans.append(node.val)
      po(root)
      return ans