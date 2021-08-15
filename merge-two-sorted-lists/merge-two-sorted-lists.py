# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val: l1, l2 = l2, l1
        head = ans = l1
        l1 = l1.next
        while l1 and l2:
          if l1.val < l2.val:
            ans.next = l1
            l1 = l1.next
          else:
            ans.next = l2
            l2 = l2.next
          ans = ans.next
        ans.next = l1 if l1 else l2
        return head