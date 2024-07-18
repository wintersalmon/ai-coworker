class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][4], self.board[4][3] = 'W', 'W'
        self.board[3][3], self.board[4][4] = 'B', 'B'

    def is_valid_move(self, row, col, color):
        if not (0 <= row < 8 and 0 <= col < 8) or self.board[row][col] == color:
            return False
        return any(self._check_line(row, col, dr, dc, color) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)])

    def _check_line(self, r, c, dr, dc, color):
        while True:
            r += dr
            c += dc
            if not (0 <= r < 8 and 0 <= c < 8):
                return False
            if self.board[r][c] == color:
                return True
            if self.board[r][c] == ' ':
                return False
