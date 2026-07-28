# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, -float('inf'))])

        while q:
            curr, highest = q.popleft()
            
            if curr.val >= highest:
                highest = curr.val
                res += 1

            if curr.left:
                q.append((curr.left, highest))
            
            if curr.right:
                q.append((curr.right, highest))



        return res