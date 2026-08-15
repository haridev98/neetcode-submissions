# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        len = 0
        dummy = ListNode(0,next = head)
        cur = head
        while cur:
            cur = cur.next
            len+=1
        if len  == 1:
            return None
        r = len  - n
        print(r)
        l = 0
        cur = dummy
        while l<r:
            l+=1
            cur = cur.next
        print(cur.val)
        next_node = cur.next
        next_next_node = cur.next.next
        next_node.next = None
        cur.next = next_next_node

        return dummy.next

            
        