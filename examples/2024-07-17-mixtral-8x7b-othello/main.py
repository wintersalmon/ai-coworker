from game import Game

def main():
    game = Game()
    while True:
        for row in range(8):
            print(" ".join(game.board.board[row]))
        print('Current player:', game.current_player)
        try:
            x, y = map(int, input('Enter your move (row col): ').split())
        except ValueError:
            print('Invalid input, try again')
            continue
        if not (0 <= x < 8 and 0 <= y < 8) or not game.play(x, y):
            print('Invalid move')

if __name__ == '__main__':
    main()