# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Empty list or one node
            if head is None or head.next is None:
                return head

            # Find length and the last node
            length = 1
            tail = head

            while tail.next:
                tail = tail.next
                length += 1

            # Remove unnecessary full rotations
            k = k % length

            # No rotation needed
            if k == 0:
                return head

            # Find the new tail
            new_tail = head

            for _ in range(length - k - 1):
                new_tail = new_tail.next

            # New head is after new tail
            new_head = new_tail.next

            # Break the list
            new_tail.next = None

            # Connect old tail to old head
            tail.next = head

            return new_head



        