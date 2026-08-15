# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast  and fast.next :
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        prev = None
        
        while l2 :
            next_node = l2.next
            l2.next = prev
            prev = l2
            l2 = next_node
        l1 = head
        l2 = prev
        while l1 and l2 :
            next_l1 = l1.next
            l1.next = l2
            l1 = next_l1
            next_l2 = l2.next
            l2.next = l1
            l2 = next_l2
        return None
        
            

        


        