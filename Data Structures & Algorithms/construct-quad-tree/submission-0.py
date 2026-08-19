"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][j + c]:
                        allSame = False
                        break

            if allSame:
                return Node(grid[r][c], True)

            n //= 2

            tL = dfs(n, r, c)
            tR = dfs(n, r, c + n)
            bL = dfs(n, r + n, c)
            bR = dfs(n, r + n, c + n)

            return Node(0, False, tL, tR, bL, bR)





        return dfs(len(grid), 0, 0)