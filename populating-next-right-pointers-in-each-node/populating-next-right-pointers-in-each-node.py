class Solution:
    def connect(self, root: 'Node') -> 'Node':
      if not root: return root
      dq = deque()
      dq.append(root)
      while dq:
        l = len(dq)
        for i in range(l):
          node = dq.popleft()
          if i != l - 1:
            node.next = dq[0]
          if node.left:
            dq.append(node.left)
          if node.right:
            dq.append(node.right)
      return root