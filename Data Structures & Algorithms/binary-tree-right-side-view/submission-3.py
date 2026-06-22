# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        q = deque([(root, 0)])
        currLevel = -1

        while q:
            curr, level = q.popleft()
            if level > currLevel:
                res.append(curr.val)
                currLevel += 1

            if curr.right:
                q.append((curr.right, level + 1))
            
            if curr.left:
                q.append((curr.left, level + 1))
            
        return res




        