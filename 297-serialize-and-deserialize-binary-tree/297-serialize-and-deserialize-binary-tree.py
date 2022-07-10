# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
      vals = []
      def pre(node):
          if node:
              vals.append(str(node.val))
              pre(node.left)
              pre(node.right)
          else:
              vals.append('#')
                
      pre(root)
      return ' '.join(vals)

    def deserialize(self, data):
      vals = iter(data.split())
      
      def depre():
          val = next(vals)
          if val == '#':
              return None
          node = TreeNode(int(val))
          node.left = depre()
          node.right = depre()
          return node
        
      return depre()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))