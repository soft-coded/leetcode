# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      if not head: return head
      n = 0
      cur = head
      while cur.next:
        cur = cur.next
        n += 1
      n += 1
      k %= n
      if k == 0: return head
      cur.next = head
      pos = n - k - 1
      cur = head
      while pos:
        cur = cur.next
        pos -= 1
      temp = cur.next
      cur.next = None
      return temp
      
      