import unittest
from board import Board
from player import Player

class TestOthello(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.player1 = Player('White')
        self.player2 = Player('Black')

    # Tests for Board class

    def test_initial_board_state(self):
        self.assertEqual(self.board.get((3, 4)), 'W')
        self.assertEqual(self.board.get((4, 5)), 'W')
        self.assertEqual(self.board.get((4, 4)), 'B')
        self.assertEqual(self.board.get((5, 4)), 'B')

    def test_valid_move(self):
        move = (4, 3)
        self.assertTrue(self.board.check_valid_move(move, self.player1))

    def test_invalid_move(self):
        move = (8, 8)
        self.assertFalse(self.board.check_valid_move(move, self.player1))

    def test_flip_discs(self):
        self.board.flip_discs((4, 3), 'W', 'B')
        self.assertEqual(self.board.get((5, 2)), 'W')
        self.assertEqual(self.board.get((6, 3)), 'W')

    def test_game_end_conditions(self):
        # Test board full
        for i in range(8):
            for j in range(8):
                self.board.set((i, j), 'W')
        self.assertTrue(self.board.check_game_end())
        # Test one color remaining
        self.board = Board()
        for i in range(4, 6):
            for j in range(4, 6):
                self.board.set((i, j), 'W')
        self.assertTrue(self.board.check_game_end())

    # Tests for Player class

    def test_pass_turn(self):
        self.player1.pass_turn()
        self.assertEqual(self.player1.get_last_move(), None)

    def test_undo_move(self):
        self.player1.make_move((4, 3))
        self.player1.undo_move()
        self.assertEqual(self.player1.get_last_move(), None)

if __name__ == '__main__':
    unittest.main()