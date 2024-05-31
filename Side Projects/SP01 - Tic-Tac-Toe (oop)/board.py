class Board:
    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    
    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")


    def print_board(self):
        print("\nPositions:\n")
        self.print_board_with_positions()

        print("\nBoard:\n")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()


    def submit_move(self, player, move):
        row = move.get_row()
        column = move.get_column()
        current_value = self.game_board[row][column]

        if current_value == Board.EMPTY_CELL:
            self.game_board[row][column] = player.marker
        else:
            print("This position is already taken! Turn lost...")


    def check_is_game_over(self, player, last_move):
        return (self.check_row(player, last_move)
                or self.check_column(player, last_move)
                or self.check_diagonal(player)
                or self.check_antidiagonal(player))


    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]
        return board_row.count(player.marker) == 3


    def check_column(self, player, last_move):
        marker_count = 0
        column_index = last_move.get_column()
        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                marker_count += 1
        return marker_count == 3


    def check_diagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                marker_count += 1
        return marker_count == 3


    def check_antidiagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                marker_count += 1
        return marker_count == 3


    def check_is_tie(self):
        empty_counter = 0
        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)

        return empty_counter == 0


    def reset_board(self):
        self.game_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]