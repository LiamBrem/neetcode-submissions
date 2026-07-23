# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            arr.append(curr)
            dfs(curr.right)


        dfs(root)
        n1, n2 = None, None

        for i in range(len(arr) - 1):
            node = arr[i]
            next = arr[i + 1]
            if next.val < node.val:
                n2 = next
                if not n1:
                    n1 = node
                else:
                    break


        n1.val, n2.val = n2.val, n1.val


        