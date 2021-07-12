class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3]] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums(self):
    # 0 | 1 | 2 etc (tells us what number correspond to what box)
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
        print( print('| ' + ' | '.join(row) + ' |'))


    def avaiable_moves(self):
        pass