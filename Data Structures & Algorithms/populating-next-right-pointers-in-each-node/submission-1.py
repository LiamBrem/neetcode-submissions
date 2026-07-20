"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        q = deque([(root, 0)])

        while q:
            curr, level = q.popleft()

            if curr.left:
                q.append((curr.left, level + 1))
                q.append((curr.right, level + 1))


            # last node of level
            if len(q) > 0 and level == q[0][1]:
                curr.next = q[0][0]



        return root

        
