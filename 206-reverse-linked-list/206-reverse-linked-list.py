# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head or not head.next:
        return head
      behind = head
      ahead = head.next
      behind.next = None
      while ahead:
        temp = ahead.next
        ahead.next = behind
        behind = ahead
        ahead = temp
      return behind