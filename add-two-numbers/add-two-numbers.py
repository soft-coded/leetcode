# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      c = 0
      head = temp = ListNode()
      while l1 or l2:
        sm = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
        c = sm // 10
        temp.val = sm % 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if l1 or l2: 
          temp.next = ListNode()
          temp = temp.next
      if c:
        temp.next = ListNode(val=c)
      return head