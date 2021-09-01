# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
      st = head
      l = 0
      while st:
        l += 1
        st = st.next
      st = head
      n = l - n
      if n == 0: return head.next
      while n > 1:
        st = st.next
        n -= 1
      st.next = st.next.next
      return head