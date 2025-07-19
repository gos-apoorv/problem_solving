# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        list_node = head
        index = 0


        while list_node:
            last_node = list_node
            list_node = list_node.next
            index += 1

        print(index)
        if index <= 1 or k % index == 0:
            return head

        swaps = k if k < index else k % index
        print(swaps)

        list_node = head
        for _ in range(1, index - swaps):
            list_node = list_node.next

        first_node = list_node.next
        last_node.next = head
        list_node.next = None

        return first_node