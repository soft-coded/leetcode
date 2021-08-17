# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
          head = head.next
        h = head
        n = head.next if head else None
        while n:
          if n.val == val:
            h.next = n.next
          else:
            h = h.next
          n = n.next
        return head