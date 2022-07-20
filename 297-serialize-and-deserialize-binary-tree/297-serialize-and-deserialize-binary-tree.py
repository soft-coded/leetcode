# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
      vals = []
      dq = deque()
      dq.append(root)
      while dq:
        node = dq.popleft()
        if not node:
          vals.append('#')
          continue
        vals.append(str(node.val))
        dq.append(node.left)
        dq.append(node.right)
      
      return " ".join(vals)

    def deserialize(self, data):
      vals = data.split()
      dq = deque()
      root = None
      if vals[0] != '#':
        root = TreeNode(int(vals[0]))
      dq.append(root)
      i = 1
      while dq and i < len(vals):
        node = dq.popleft()
        left = vals[i]
        right = vals[i + 1]
        i += 2
        if left != '#':
          node.left = TreeNode(int(left))
          dq.append(node.left)
        if right != '#':
          node.right = TreeNode(int(right))
          dq.append(node.right)      
        
      return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))