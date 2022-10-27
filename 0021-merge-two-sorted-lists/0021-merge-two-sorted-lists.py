# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        h1 = list1
        h2 = list2
        if h1.val > h2.val:
            h1, h2 = h2, h1
            
        ans = cur = h1
        h1 = h1.next
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next

        while h1:
            cur.next = h1
            h1 = h1.next
            cur = cur.next
        
        while h2:
            cur.next = h2
            h2 = h2.next
            cur = cur.next
        
        cur.next = None
        return ans
        
        
        
        
        