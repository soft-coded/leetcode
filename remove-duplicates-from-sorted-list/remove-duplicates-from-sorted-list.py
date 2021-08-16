# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        s = {head.val}
        h = head
        prev = h
        h = h.next
        while h:
          if h.val not in s:
            prev.next = h
            prev = prev.next
            s.add(h.val)
          else:
            prev.next = h.next
          h = h.next
        return head