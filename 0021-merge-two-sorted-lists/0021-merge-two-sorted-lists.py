# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            if  l1 == None or l2 == None:
                if l1:
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                    l1 = l1.next if l1 else None
                else:
                    cur.next = ListNode(l2.val)
                    cur =  cur.next
                    l2 = l2.next if l2 else None
            elif v1 == v2:
                cur.next = ListNode(v1)
                cur = cur.next
                l1 = l1.next if l1 else None
            elif v1 > v2:
                cur.next = ListNode(v2)
                cur = cur.next
                l2 = l2.next if l2 else None
            else:
                cur.next = ListNode(v1)
                cur = cur.next
                l1 = l1.next if l1 else None
            

        return dummy.next
