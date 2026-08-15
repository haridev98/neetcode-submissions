# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        if curr_1 == None :
            return curr_2
        elif curr_2 == None:
            return curr_1
        output = None
        head = None
        while curr_1 and curr_2:
            if curr_1.val <= curr_2.val :
                if output == None:
                    head = output = curr_1
                else:
                    output.next = curr_1
                    output  = curr_1
                curr_1 = curr_1.next
            else:
                if output == None:
                    head = output = curr_2
                else:
                    output.next = curr_2
                    output = curr_2
                curr_2 = curr_2.next
        if curr_1 != None:
            output.next = curr_1
        if curr_2 != None:
            output.next = curr_2
        
        return head
        