class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j):
            if i >= rows or i < 0 or j >= cols or j < 0:
                return 0

            if (i, j) in visited:
                return 0

            if grid[i][j] == 0:
                return 0

            visited.add((i, j))            

            curr = 1 
            for dx, dy in dirs:
                if (i + dx, j + dy) not in visited:
                    curr += dfs(i + dx, j + dy)
            
            return curr





        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited:
                    res = max(res, dfs(row, col))


        return res
        