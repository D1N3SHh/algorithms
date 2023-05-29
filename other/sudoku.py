# recursive algorithm to generate valid sudoku board
# time complexity: 
# auxiliary space: 


import random


class generate_sudoku():
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.generate(self.board)
        self.print_board()

    def __repr__(self):
        return str(self.board)

    def is_valid(self, board, row, col, num):
        # check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # check 3x3 block
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    # recursive function
    def generate(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.generate(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(row)


if __name__ == "__main__":
    generate_sudoku()