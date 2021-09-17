# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      vals = []
      h = head
      while h:
        vals.append(h.val)
        h = h.next
      vals.sort()
      cur = dummy = ListNode()
      for item in vals:
        cur.next = cur = ListNode(item)
      return dummy.next