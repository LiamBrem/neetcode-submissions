"""
Edge cases:
- Contain only chars
- board and board[0] will always be >0

Solution:
- loop through the board and start at each letter (if matching)
- perform dfs()
- keep track of current index and if make it to the end, return true

["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(row, col, i):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return False

            if (row, col) in seen:
                return False

            if board[row][col] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            seen.add((row, col))

            res = False

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = row + dr, col + dc

                res |= dfs(nr, nc, i + 1)

            seen.remove((row, col))

            return res
        

        for row in range(rows):
            for col in range(cols):
                seen = set()
                if dfs(row, col, 0):
                    return True


        return False