# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        if head.next == None:
            head = head.next
        else:
            while n != 0:
                fast = fast.next 
                n -= 1
            if fast == None:
                slow = slow.next
                head = head.next
            else:
                while fast.next:
                    fast = fast.next
                    slow = slow.next
                slow.next = slow.next.next
        return head