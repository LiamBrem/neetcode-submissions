class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row,col))

        while q:
            cr, cc = q.popleft()

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if grid[nr][nc] != 2147483647:
                    continue


                grid[nr][nc] = grid[cr][cc] + 1

                q.append((nr, nc))
                    


        


