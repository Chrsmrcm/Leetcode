# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        solution = ListNode()
        active = solution

        while list1 and list2:
            if list1.val < list2.val:
                active.next = list1
                list1 = list1.next
            else:
                active.next = list2
                list2 = list2.next
            
            active = active.next

        if list1:
            active.next = list1
        else:
            active.next = list2

            
        return solution.next
            



