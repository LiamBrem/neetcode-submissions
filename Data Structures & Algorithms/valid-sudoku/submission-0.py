class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for row in range(rows):
            seen = set()
            for col in range(cols):
                val = board[row][col]
                if val == '.':
                    continue

                if val in seen or not (0 <= int(val) <= 9):
                    return False

                seen.add(val)

        for col in range(cols):
            seen = set()
            for row in range(rows):
                val = board[row][col]
                if val == '.':
                    continue

                if val in seen or not (0 <= int(val) <= 9):
                    return False

                seen.add(val)

        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                seen = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        val = board[row][col]
                        if val == '.':
                            continue
        
                        if val in seen or not (0 <= int(val) <= 9):
                            return False
        
                        seen.add(val)

        return True