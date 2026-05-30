# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- given root
- can't just iterate down the rightmost branch
- can perform a dfs and keep track of the level
- build out some sort of 2d arrays with nodes by level
- and then append the rightmost (arr[-1]) to the result and return it
- how do we know it's the rightmost?
    - we do a pre-order traversal so we're always hitting the left
    nodes first and then just append to the arrays right to left

or:
- do a bfs and keep track of the level
- go right to left and only append the first right node to the res
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        currLevel = 0
        q = deque()

        q.append((root, 1))

        while q:
            node, level = q.popleft()

            if level != currLevel:
                currLevel += 1
                res.append(node.val)

            if node.right: 
                q.append((node.right, level + 1))

            if node.left: 
                q.append((node.left, level + 1))

        
        return res

            
        