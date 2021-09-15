class Solution:
    def cloneGraph(self, node):
      self.d = {}
      return self.clone(node)
    
    def clone(self, node):
      if not node: return node
      if node.val in self.d: return self.d[node.val]
      
      n = Node(node.val)
      self.d[node.val] = n
      for item in node.neighbors:
        n.neighbors.append(self.clone(item))
      return n