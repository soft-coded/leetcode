# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
      if not head: return head
      s = []
      l = []
      h = head
      while h:
        if h.val < x:
          s.append(h.val)
        else:
          l.append(h.val)
        h = h.next
      ans = None
      for item in reversed(l):
        temp = ListNode(val=item)
        temp.next = ans
        ans = temp
      for item in reversed(s):
        temp = ListNode(val=item)
        temp.next = ans
        ans = temp
      return ans