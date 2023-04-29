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
    TODO: explain what the class is about, definition of various terms
    etc
    '''

    def __init__(self):
        self.nsize = 3
        self._board = []
        for r in range(self.nsize):
            self._board.append(['' for c in range(self.nsize)])

        # set the board to its initial state
        self.reset()

    def display(self):
        '''
        display the game board which will look like something like this

           1 | X | 3
           4 | 5 | O
           7 | 8 | 9

        '''
        num = 1
        for row in self._board:
            for place in row:
                print("|", num, "|", end='')
                num += 1
            print()

    def reset(self):
        '''
        Reset the game board so that each cell is index from 1 to 9.
        So when display it will look like

           1 | 2 | 3
           4 | 5 | 6
           7 | 8 | 9

        '''
        count = 1
        for r in range(self.nsize):
            for c in range(self.nsize):
                self._board[r][c] = count
                count += 1

    def place_into(self, symbol, spot):
        '''
        Find the cell that spot is located, then replace the cell by
        the symbol X or O
        '''
        for r in range(self.nsize):
            for c in range(self.nsize):
                if self._board[r][c] == spot:
                    self._board[r][c] = symbol.value

    def has_winner(self):
        '''
        Determine if one side has won (ie a winning row, column or a winning diagonal.
        If there is a winner, display who is the winner and return true
        otherwise return false
        '''
        # first row check
        if (self._board[0][0] == self._board[0][1] and self._board[0][0] == self._board[0][2]):
            return True
        # second row check
        if (self._board[1][0] == self._board[1][1] and self._board[1][0] == self._board[1][2]):
            return True
        # third row check
        if (self._board[2][0] == self._board[2][1] and self._board[2][0] == self._board[2][2]):
            return True

        # first column check
        if (self._board[0][0] == self._board[1][0] and self._board[0][0] == self._board[2][0]):
            return True
        # second column check
        if (self._board[0][1] == self._board[1][1] and self._board[0][1] == self._board[2][1]):
            return True
        # third column check
        if (self._board[0][2] == self._board[1][2] and self._board[0][2] == self._board[2][2]):
            return True

        # check the diagonals
        if (self._board[1][1] == self._board[0][0] and self._board[1][1] == self._board[2][2]):
            return True
        if (self._board[1][1] == self._board[2][0] and self._board[1][1] == self._board[0][2]):
            return True

        return False


    def is_valid(self, spot):
        '''
        return true if spot is a valid location that you can place a symbol into
        ie. it has not been occupied by an X or an O
        '''
        num= 1
        for row in self._board:
            for place in row:
                if num == spot:
                    return True
                num += 1
        return False


def run():

    count = 0
    turn = GamePiece.CROSS

    start = input("Do you want to play Tic-Tac-Toe? (y/n) \n")
    if start.lower() == "y":
        board = GameBoard()
        board.display()

        while count < 9:

            print(f"It is {turn} turn. Which spot you want to pick?")
            spot = int(input())

            if board.is_valid(spot):
                board.place_into(turn, spot)

                #check if there is a winner, if yes, announce who is the winner
                # and close the game, otherwise set the turn to the other player
                if board.has_winner(turn):
                    print('Board has winner: ', turn, " player")
                    break

                count = count + 1
                if turn == GamePiece.CROSS:
                    turn = GamePiece.CIRCLE
                elif turn == GamePiece.CIRCLE:
                    turn = GamePiece.CROSS

            else:
                print("Invalid spot. Please try again")

        if count == 9:
            print("The game is tied")

if __name__ == "__main__":
    run()