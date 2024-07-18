from board import Board

class Game:
    def __init__(self, board=None):
        if not board:
            self.board = Board()
        else:
            self.board = board
        self.current_player = 'W'

    def play(self, row, col):
        if not self.board.is_valid_move(row, col, self.current_player):
            return False
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if self._flip_discs(row, col, dr, dc):
                self.board.board[row][col] = self.current_player
                self.current_player = 'B' if self.current_player == 'W' else 'W'
                return True

    def _flip_discs(self, row, col, dr, dc):
        r, c = row + dr, col + dc
        while 0 <= r < 8 and 0 <= c < 8:
            if self.board.board[r][c] == ' ' or self.board.board[r][c] != self.current_player:
                break
            self.board.board[r][c] = self.board.board[row][col]
            r, c = r + dr, c + dc
        return r >= 0 and c >= 0