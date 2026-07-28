# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, highest):
            if not curr: 
                return 0

            if curr.val >= highest:
                self.res += 1
                highest = curr.val
            
            dfs(curr.left, highest)
            dfs(curr.right, highest)



        dfs(root, float('-inf'))

        return self.res