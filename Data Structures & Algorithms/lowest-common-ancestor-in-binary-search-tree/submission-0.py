# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def treeContains(root, target):
            if not root:
                return False

            qu = deque([root])

            while qu:
                curr = qu.popleft()

                if curr.val == target.val:
                    return True

                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)

            return False


        def dfs(curr):
            if curr.val == p.val or curr.val == q.val:
                return curr
            elif treeContains(curr.left, p) and treeContains(curr.left, q):
                return dfs(curr.left)
            elif treeContains(curr.right, p) and treeContains(curr.right, q):
                return dfs(curr.right)
            else:
                return curr

        return dfs(root)