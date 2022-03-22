from MSsquare import MSsquare
import random


class GameField:
    """represents the board of the game"""

    def __init__(self, size=4, mines=8):
        self.__size = size
        self.__mines = mines
        self.__exposed = 0
        # creates nested list, every object is a MSsqare
        self.__field = [[self.create_sqr() for j in range(self.__size)] for i in range(self.__size)]

    @property
    def size(self):
        return self.__size

    @property
    def mines(self):
        return self.__mines

    def mines_random(self):
        """spreads randomly the mines in the field"""
        for num in range(self.mines):  # choose random location for every mine
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            self.field[row][col].has_mine = True

    def sqr_val(self):
        """sets the number of a square, according to how many mines near it."""
        for row in range(self.size):  # runs on every single square in the field
            for col in range(self.size):
                if self.field[row][col].has_mine:
                    continue
                    # checks for every near square if it has a mine.
                # if so, increasing square.neighbor_mines by 1
                if row > 0 and self.field[row - 1][col].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if row < self.size - 1 and self.field[row + 1][col].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if col > 0 and self.field[row][col - 1].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if col < self.size - 1 and self.field[row][col + 1].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if row > 0 and col > 0 and self.field[row - 1][col - 1].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if row > 0 and col < self.size - 1 and self.field[row - 1][col + 1].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if row < self.size - 1 and col > 0 and self.field[row + 1][col - 1].has_mine:
                    self.field[row][col].neighbor_mines += 1
                if row < self.size - 1 and col < self.size - 1 and self.field[row + 1][col + 1].has_mine:
                    self.field[row][col].neighbor_mines += 1

    @property
    def field(self):
        return self.__field

    # @property
    # def score(self):
    #     return self.__score
    #
    # @score.setter
    # def score(self, val):
    #     self.score += val

    def create_sqr(self):
        xy = MSsquare()
        return xy

    def print(self):
        """prints the board on the screen"""
        line = '  ' + '-----'.join('+' * (self.__size + 1))
        print(line)
        for i in range(len(self.field)):  # prints row number
            print(i + 1, '|', end='')
            for j in self.field[i]:  # prints the squares in a row
                print(str(j), end='')
                print('|', end='')
            print('\n' + line)
        bottom = ''
        for i in range(self.size):  # prints letters, representing columns
            bottom += '     ' + (chr(ord('A') + i))
        print(bottom)

    def has_exposed(self):
        """counts how many squares has already been choosen"""
        return self.__exposed

    def expose(self, x, y):
        """turn square.hidden to True.
        if no mines surround it, expose near squares recursively"""
        sqr = self.field[x][y]
        if sqr.has_mine:
            return
        if sqr.hidden:
            self.__exposed += 1
            sqr.hidden = False

            if sqr.neighbor_mines != 0:
                return
            if sqr.neighbor_mines == 0:
                if x > 0:
                    self.expose(x - 1, y)
                if x < self.size - 1:
                    self.expose(x + 1, y)
                if y > 0:
                    self.expose(x, y - 1)
                if y < self.size - 1:
                    self.expose(x, y + 1)
                if x > 0 and y > 0:
                    self.expose(x - 1, y - 1)
                if x > 0 and y < self.size - 1:
                    self.expose(x - 1, y + 1)
                if x < self.size - 1 and y > 0:
                    self.expose(x + 1, y - 1)
                if x < self.size - 1 and y < self.size - 1:
                    self.expose(x + 1, y + 1)
        return

    def expose_all(self):
        """turn all squares to not hidden"""
        for row in self.field:  # runs on every single square
            for col in row:
                col.hidden = False