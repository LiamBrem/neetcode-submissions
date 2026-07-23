"""
only the largest gap is the effort

brute force:
- try all paths
- keep track of current path but max

another way:
- bfs with min heap - choose the shortest each time until end is reached

"""
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        res = 0
        rows, cols = len(heights), len(heights[0])
        seen = set()
        q = [(0, heights[0][0], 0, 0)] # nextDist, prevDist, nextRow, nextCol

        while q:
            dist, prevHeight, row, col = heapq.heappop(q)
            height = heights[row][col]
            res = max(res, abs(height - prevHeight))

            if row == rows - 1 and col == cols - 1:
                break

            if (row, col) in seen:
                continue

            seen.add((row, col))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = row + dr, col + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                newDist = abs(heights[nr][nc] - height)
                heapq.heappush(q, (newDist, height, nr, nc))


        return res
