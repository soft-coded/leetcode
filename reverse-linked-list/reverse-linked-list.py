# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        p = head
        n = head.next
        while n:
          temp = n
          n = n.next
          temp.next = p
          p = temp
        head.next = None
        return p