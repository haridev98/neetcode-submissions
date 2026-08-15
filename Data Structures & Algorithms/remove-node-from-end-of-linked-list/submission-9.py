# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast =  slow  = dummy= ListNode(val = 0 , next = head)
        for i in range(n):
            fast = fast.next
            #print(i,fast.val)
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        next_node  =  slow.next
        slow.next = slow.next.next
        next_node.next = None

        return dummy.next 
        
