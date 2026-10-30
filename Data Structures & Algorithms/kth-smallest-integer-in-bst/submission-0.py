# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        self.counter = 0

        def dfs(curr):
            if not curr:
                return None

            left = dfs(curr.left)
            if left is not None:
                return left

            self.counter += 1

            
            if self.counter == k:
                return curr.val

            return dfs(curr.right)

        return dfs(root)

        