# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def find_len(head):
    l = 0
    prev = None
    while head:
        l += 1
        prev = head
        head = head.next
    
    return (l, prev)
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        l, tail = find_len(head)
        k %= l
        
        tail.next = head
        cur = head
        pos = l - k - 1
        while pos:
            cur = cur.next
            pos -= 1
        
        new_head = cur.next
        cur.next = None
        return new_head
            
        
        
        
        
        