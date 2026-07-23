# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            v1, v2 = curr.val, curr.next.val
            gcd = math.gcd(v1, v2)
            newNode = ListNode(gcd)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        return head

        