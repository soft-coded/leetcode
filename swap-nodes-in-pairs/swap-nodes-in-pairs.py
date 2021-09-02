# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head or not head.next: return head
      cur = head
      head = cur.next
      prev = cur
      while cur and cur.next:
        temp = cur.next.next
        cur.next.next = cur
        prev.next = cur.next
        cur.next = temp
        prev = cur
        cur = cur.next
      return head