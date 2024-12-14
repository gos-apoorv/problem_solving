# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Progress through LinkedList in 1 step
        step_1 = head
        # Progress through LinkedList in 2 step
        step_2 = head

        while step_2.next != None and step_2.next.next != None:
            step_1 = step_1.next
            step_2 = step_2.next.next

        if step_2.next is not None:
            step_1 = step_1.next

        return step_1