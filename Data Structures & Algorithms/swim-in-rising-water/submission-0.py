"""
grid[i][j] = elevation
rain starts to fall at time t = 0
at any point in time t, all squares <= t are swimmable
can swim in any direction

Goal: find a path with the smallest max square

Brute force:
- check all paths from start to finish bfs or dfs
- keep track of the max for each path
- after all paths are checked return the smallest max

"""
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0)) # "distance", i, j
        dists = [[float('inf')] * cols for _ in range(rows)]
        dists[0][0] = grid[0][0]

        while heap:
            distance, i, j = heapq.heappop(heap)

            if distance > dists[i][j]:
                continue

            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                    continue

                newDist = max(grid[ni][nj], distance)

                if newDist < dists[ni][nj]:
                    dists[ni][nj] = newDist
                    heapq.heappush(heap, (newDist, ni, nj))


        return dists[-1][-1]

        
