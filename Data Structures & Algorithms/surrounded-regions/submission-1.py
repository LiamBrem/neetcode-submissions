class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def bfs(row, col):
            seen = {(row, col)}

            q = deque([(row, col)])

            while q:
                r, c = q.popleft()

                for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dy, c + dx
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if board[nr][nc] == "X":
                        continue

                    if (nr, nc) in seen:
                        continue

                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return
                    
                    seen.add((nr, nc))
                    q.append((nr, nc))


            for r, c, in seen:
                board[r][c] = "X"


        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if board[row][col] == "O":
                    bfs(row, col)

