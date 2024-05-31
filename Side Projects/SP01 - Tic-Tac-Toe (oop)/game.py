from board import Board
from player import Player


class TicTacToeGame:

    def start(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("    Welcom to Tic-Tac-Toe    ")
        print(".............................")

        board = Board()
        player = Player()
        computer = Player(False)


        while True:        # ask if the user would like to continue the game
            board.print_board()
            while True:        # for game logic: get move, check tie, check won
                player_move = player.get_human_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_game_over(player, player_move):
                    print("\nAwesome! You won the game.")
                    break
                elif board.check_is_tie():
                    print("\nIt's a tie! Try again.")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print("\nOops... The computer won.\nTry again.")
                        break

            play_again = input("\nWould you like to play again? Enter 'X' for YES or 'O' for NO: ").upper()
            if play_again == 'O':
                break
            else:
                self.start_new_round(board)



    def start_new_round(self, board):
        print("\n*****************")
        print("    New Round    ")
        print("*****************")
        board.reset_board()