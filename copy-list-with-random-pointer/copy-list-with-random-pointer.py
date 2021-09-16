"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
      if not head: return head
      h, ind, nodes, i = head, {}, [], 0
      while h:
        h.index = i
        i += 1
        h = h.next
      h, i = head, 0
      while h:
        if h.random:
          ind[i] = h.random.index
        h = h.next
        i += 1
      cur = Node(-1)
      h = head
      while h:
        cur.next = cur = Node(h.val)
        nodes.append(cur)
        h = h.next
      for key, val in ind.items():
        nodes[key].random = nodes[val]
      return nodes[0]