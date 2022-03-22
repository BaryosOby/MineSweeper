from GameField import *

title = '''___  ____            _____                                   
|  \/  (_)          /  ___|                                  
| .  . |_ _ __   ___\ `--.__      _____  ___ _ __   ___ _ __ 
| |\/| | | '_ \ / _ \`--. \ \ /\ / / _ \/ _ \ '_ \ / _ \ '__|
| |  | | | | | |  __/\__/ /\ V  V /  __/  __/ |_) |  __/ |   
\_|  |_/_|_| |_|\___\____/  \_/\_/ \___|\___| .__/ \___|_|   
                                            | |              
                                            |_|'''


def size_check(num):
    """check size input validation"""
    try:  # checks if input is an integer
        if int(num) in [4, 5, 6, 7, 8, 9]:  # checks if size in right range
            return True
        print('\nsize must be between 4 to 9', end='\n')
        return False
    except:
        print('mines number must be an integer', end='\n')
        return False


def mines_check(num, size):
    """check mines input validation"""
    try:  # checks if input is an integer
        if int(num) in range(1, size * 2 + 1):  # checks if mines in right range
            return True
        print('\n'f'mines number must be between 1 to {size * 2}', end='\n')
        return False
    except:
        print('\nmines number must be an integer', end='\n')
        return False


def cords_check(inp, size):
    """check mines input validation"""
    if len(str(inp)) != 2:  # checks if input in correct format
        print("\ncords must be in format of '1A'", end='\n')
        return False
    if ord(inp[1].upper()) not in range(ord('A'), ord('A') + size):
        # checks if letter in right range
        print('\ncolumn cord out of range', end='\n')
        return False
    try:  # checks if first character is an integer
        num = int(inp[0])
        if num > size or num < 0:  # checks if number in right range
            print('\nrow cord out of range', end='\n')
            return False
        return True
    except:
        print('\nrow cord must be an integer', end='\n')
        return False


def main():
    print(title)

    size = input('''Welcome to Mine Sweeper!
choose field size between 4 to 9: ''')

    while not size_check(size):
        # checks the input, if it's not valid, ask for new one
        size = input('Please enter an integer between 4 to 9: ')
    size = int(size)
    mines = input(f'Enter mines number between 1 to {2 * int(size)}: ')
    while not mines_check(mines, size):
        # checks the input, if it's not valid, ask for new one
        mines = input(f'Please enter an integer between 1 to {2 * int(size)}: ')
    mines = int(mines)

    # sets game details
    game = GameField(size, mines)
    board = game.field
    count = 0
    game.mines_random()
    game.sqr_val()
    max_points = game.size ** 2 - mines

    # the game itself:
    game_over = False
    while not game_over:  # runs until game is over, win or lose
        game.print()
        cords = input("enter row number and column letter (example: 1A): ")
        while not cords_check(cords, game.size):
            # checks the input, if it's not valid, ask for new one
            cords = input('enter row number and column letter (example: 1A): ')
        row = int(cords[0]) - 1
        col = ord(cords[1].upper()) - ord('A')

        if board[row][col].has_mine:  # user landed on a mine
            game_over = True

        elif not board[row][col].hidden:  # user chose an exposed square
            print('Square is alredy exposed')

        else:
            game.expose(row, col)
            count = game.has_exposed()
            print(count)
            if count == max_points:  # checks if all squares exposed
                game_over = True

    game.expose_all()
    game.print()
    if count == max_points:
        print(f'''Congratulations! You Won!
Your score is {max_points} out of {max_points}''')
    else:
        print(f'''BOOM! You landed on a mine!
Game is over, your score is {count} out of {max_points}''')


if __name__ == '__main__':
    main()