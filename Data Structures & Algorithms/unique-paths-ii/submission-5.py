class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        grid = [[0] * cols for _ in range(rows)]
        grid[0][0] = 1

        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col] == 1 or (row == 0 and col == 0):
                    continue

                elif row == 0:
                    grid[row][col] = grid[row][col - 1]
                
                elif col == 0:
                    grid[row][col] = grid[row - 1][col]

                else:
                    grid[row][col] = grid[row - 1][col] + grid[row][col - 1]


        return grid[-1][-1]
        