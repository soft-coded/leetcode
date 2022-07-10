"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
      self.visited = {}
      return self.clone(node)
    
    def clone(self, node):
      if not node: 
        return None
      if node.val in self.visited: 
        return self.visited[node.val]
      
      n = Node(node.val)
      self.visited[node.val] = n
      
      for item in node.neighbors:
        n.neighbors.append(self.clone(item))
        
      return n