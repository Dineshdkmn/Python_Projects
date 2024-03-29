import random
import re

class Minesweeper:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc %  self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'  # Place a bomb
            bombs_planted += 1  # Increment the bombs planted counter
            
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue

                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0 

        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if r == row and c == col:
                    continue

                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
            
        return num_neighboring_bombs

    def dig(self, row, col):
        if (row, col) in self.dug:
            return True

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False

        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board =[[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])

        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format_str = '%-' + str(widths[idx]) + "s"
            cells.append(format_str % col)
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format_str = '%-' + str(widths[idx]) + "s"
                cells.append(format_str % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep

def play():
    try:
        dim_size = int(input("Enter the dimension size of the board: "))
        num_bombs = int(input("Enter the number of bombs: "))
    except ValueError:
        print("Invalid input. Please enter integers for dimension size and number of bombs.")
        return

    board = Minesweeper(dim_size, num_bombs)

    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)

        try:
            user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col: "))
            row, col = int(user_input[0]), int(user_input[-1])
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column separated by a comma.")
            continue

        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again!")
            continue

        safe = board.dig(row, col)

        if safe:
            bombs_left = num_bombs - len(board.dug.intersection(board.dug))
            print(f"You have {bombs_left} bombs left to win!")
        else:
            print("Sorry Game Over :(")
            # Reveal all bombs
            for r in range(board.dim_size):
                for c in range(board.dim_size):
                    if board.board[r][c] == '*':
                        board.dug.add((r, c))
            print(board)
            break

    if safe:
        print("Congratulations!!! You are victorious!")

if __name__ == "__main__":
    play()
