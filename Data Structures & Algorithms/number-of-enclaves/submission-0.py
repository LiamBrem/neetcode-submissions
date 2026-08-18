class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return float('inf')
            
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            res = 1

            for dx, dy in dirs:
                nx, ny = row + dx, col + dy
                res += dfs(nx, ny)

            return res


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    amt = dfs(row, col)
                    if amt != float('inf'):
                        res += amt

        return res