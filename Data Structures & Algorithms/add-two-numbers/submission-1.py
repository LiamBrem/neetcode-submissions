# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = curr = ListNode()

        p1 = l1
        p2 = l2
        carry = None

        while p1 or p2 or carry:
            total = 0

            if carry:
                total += carry
                carry = None
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next

            if total >= 10:
                carry = total // 10
                total %= 10

            curr.next = ListNode(total)
            curr = curr.next


        return dummy.next
                