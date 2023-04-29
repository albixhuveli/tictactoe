'''

@project       : Queens College CSCI 381/780 Machine Learning
@Instructor    : Dr. Alex Pang

@Date          : Spring 2022

A Object-Oriented Implementation of the TicTacToe Game

references

'''

import enum


class GamePiece(enum.Enum):
    CROSS = "X"
    CIRCLE = "O"


class GameBoard(object):
    '''
    Class instance of a Tic Tac Toe board. Represented by 1-9, X or 0

           1 | 2 | 3
           4 | 5 | O
           7 | 8 | 9
    '''

    def __init__(self):
        self.nsize = 3
        self._board = []
        for r in range(self.nsize):
            self._board.append(['' for c in range(self.nsize)])

        # set the board to its initial state

    def display(self):
        '''
        display the game board which will look like something like this

           1 | X | 3
           4 | 5 | O
           7 | 8 | 9

        '''

        # TODO

        num = 1
        for row in self._board:
            for r in range(len(row)):
                if row[r] == '':
                    if (r < len(row)-1):
                        print(num, "| ",end='')
                    else:
                        print(num, end='')
                else:
                    piece = "0" if (row[r] == GamePiece.CIRCLE) else "X"
                    if (r < len(row) -1):
                        print(piece, "| ", end='')
                    else:
                        print(piece, end=' ')
                num += 1
            print()
        # end TODO

    def reset(self):
        '''
        Reset the game board so that each cell is index from 1 to 9.
        So when display it will look like

           1 | 2 | 3
           4 | 5 | 6
           7 | 8 | 9

        '''

        # TODO
        GameBoard.display(self)
        # end TODO

    def place_into(self, symbol, spot):
        '''
        Find the cell that spot is located, then replace the cell by
        the symbol X or O
        '''

        # TODO
        num = 1

        for row in self._board:
            for r in range(len(row)):
                if num == int(spot):
                    row[r] = symbol
                num += 1
        self.display()

        # end TODO

    def has_winner(self, player=None):
        '''
        Determine if one side has won (ie a winning row, column or a winning diagonal.
        If there is a winner, display who is the winner and return true
        otherwise return false
        '''
        # TODO
        win = None

        n = self.nsize
        # checking columns
        for y in range(n):
            win = True
            for x in range(n):
                if self._board[x][y] != player:
                    win = False

            if win:
                return True

        # checking rows
        for x in range(n):
            win = True
            for y in range(n):
                if self._board[x][y] != player:
                    win = False
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self._board[i][i] != player:
                win = False

        if win:
            return win

        win = True
        for i in range(n):
            if self._board[i][n - 1 - i] != player:
                win = False

        if win:
            return win
        return False
        # return False
        # end TODO

    def is_valid(self, spot):
        '''
        return true if spot is a valid location that you can place a symbol into
        ie. it has not been occupied by an X or an O
        '''

        # TODO
        num = 1
        for row in self._board:
            for r in range(len(row)):
                if (num == int(spot)):
                    if (row[r] == ''):
                        return True
                    return False
                num += 1
        return False
        # end TODO


def run():
    count = 0
    turn = GamePiece.CROSS

    start = input("Do you want to play Tic-Tac-Toe? (y/n): ")
    if start.lower() == "y":
        board = GameBoard()
        board.display()

        while count < 9:

            print(f"It is {turn} turn. Which spot you want to pick?")
            spot = input()

            if board.is_valid(spot):
                board.place_into(turn, spot)

                # check if there is a winner, if yes, announce who is the winner
                # and close the game, otherwise set the turn to the other player

                # TODO
                if board.has_winner(turn):
                    print('Board has winner: ', turn, " player")
                    break
                # end TODO

                count = count + 1
                if turn == GamePiece.CROSS:
                    turn = GamePiece.CIRCLE
                elif turn == GamePiece.CIRCLE:
                    turn = GamePiece.CROSS

            else:
                print("Invalid spot. Please try again")

        # TODO announce it is a tie game
        if count == 9:
            print("It is a tie game.")
        # end TODO

if __name__ == "__main__":
    run()