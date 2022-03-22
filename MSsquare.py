class MSsquare:
    """represents a square on the field"""

    def __init__(self):
        self.__has_mine = False
        self.__hidden = True
        self.__neighbor_mines = 0

    @property
    def has_mine(self):
        return self.__has_mine

    @has_mine.setter
    def has_mine(self, value):
        self.__has_mine = value

    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter
    def hidden(self, value):
        self.__hidden = value

    @property
    def neighbor_mines(self):
        return self.__neighbor_mines

    @neighbor_mines.setter
    def neighbor_mines(self, num):
        self.__neighbor_mines = num

    def __str__(self):
        if not self.hidden:
            if self.has_mine:
                return '  X  '  # presents square with mine as X
            else:
                # presents square without mine as how many mines surround it
                return f'  {self.__neighbor_mines}  '
        return '     '  # square not chosen yet