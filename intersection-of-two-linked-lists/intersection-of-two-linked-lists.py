# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, h1: ListNode, h2: ListNode) -> ListNode:
        if h1 is None or h2 is None:
          return None
        h11 = h1
        h22 = h2
        while h11 is not h22:
          h11 = h2 if not h11 else h11.next
          h22 = h1 if not h22 else h22.next
        return h11