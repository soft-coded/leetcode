# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      c = {}
      h = head
      while h:
        c[h.val] = c.get(h.val, 0) + 1
        h = h.next
      
      dummy = ans = ListNode(0)
      for key, val in c.items():
        if val > 1:
          continue
        ans.next = ListNode(key)
        ans = ans.next
      return dummy.next