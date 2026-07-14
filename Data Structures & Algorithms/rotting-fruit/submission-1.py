class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque() 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((0, row, col))

        level = 0

        while q:
            level, row, col = q.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow, newCol = row + dx, col + dy

                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                    continue

                if grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    q.append((level + 1, newRow, newCol))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1


        return level
        