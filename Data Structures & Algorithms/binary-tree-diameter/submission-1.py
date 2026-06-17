# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def maxDepth(curr):
            if not curr:
                return 0

            return 1 + max(maxDepth(curr.left), maxDepth(curr.right))

        def dfs(curr):
            if not curr:
                return

            self.max = max(self.max, maxDepth(curr.left) + maxDepth(curr.right))
            dfs(curr.left)
            dfs(curr.right)


        dfs(root)
        return self.max
        