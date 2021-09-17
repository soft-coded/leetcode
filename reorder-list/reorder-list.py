class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        h = head
        while h:
          nodes.append(h)
          h = h.next
        n = len(nodes)
        h = head
        for i in range(1, n // 2 + 1):
          h.next = nodes[n-i]
          h.next.next = nodes[i]
          h = h.next.next
        h.next = None
        return head