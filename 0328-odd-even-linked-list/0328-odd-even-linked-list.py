# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_head = odd_cur = head
        even_head = even_cur = head.next
        cur = head.next.next
        odd_cur.next = None
        even_cur.next = None
        odd = True
        
        while cur:
            if odd:
                odd_cur.next = cur
                odd_cur = odd_cur.next
            else:
                even_cur.next = cur
                even_cur = even_cur.next
            cur = cur.next
            odd_cur.next = None
            even_cur.next = None
            odd = not odd
        
        odd_cur.next = even_head
        return odd_head