class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        safe = set()
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if board[row][col] == "X":
                return

            if (row, col) in safe:
                return

            safe.add((row, col))
            
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = row + dy, col + dx
                dfs(ny, nx)
           
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    dfs(row, col)


        for row in range(rows):
            for col in range(cols):
                if (row, col) not in safe:
                    board[row][col] = "X"


