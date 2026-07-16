# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(n1, n2):
            if not n2 and not n1:
                return True
            
            if not n1 or not n2:
                return False

            return n2.val == n1.val and isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right)


        def dfs(curr):
            if not curr:
                return False

            if isEqual(curr, subRoot):
                return True

            return dfs(curr.left) or dfs(curr.right)


        return dfs(root)





        