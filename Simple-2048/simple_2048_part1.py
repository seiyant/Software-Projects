# student name:   Seiya Nozawa-Temchenko
# student number: 34838482

# A command-line 2048 game

import random

board: list[list] = []  # a 2-D list to keep the current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and prints a welcome message
    """
    # initialize the board cells with ''
    for _ in range(4):     
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)
    # add two starting 2's at random cells
    twoRandomNumbers = random.sample(range(16), 2)   # randomly choose two numbers between 0 and 15   
    # correspond each of the two random numbers to the corresponding cell
    twoRandomCells = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4),
                      (twoRandomNumbers[1]//4,twoRandomNumbers[1]%4))
    for cell in twoRandomCells:  # put a 2 on each of the two chosen random cells
        board[cell[0]][cell[1]] = 2

    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """
    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer until a valid next move or Q (to quit) is selected
        (valid move direction: one of 'W', 'A', 'S' or 'D')
        returns the user input
    """
    print("Enter one of WASD (move direction) or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q'): # a valid move direction or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
    return move


def addANewTwoToBoard() -> None:
    """ 
        adds a new 2 at an available randomly-selected cell of the board
    """
    empty_cells = []
    for row in range(4):
        for column in range(4):
            if board[row][column] == '':
                empty_cells.append((row, column)) #check empty cells

    if not empty_cells:
        return
    
    add_cell = random.choice(empty_cells)
    board[add_cell[0]][add_cell[1]] = 2

def isFull() -> bool:
    """ 
        returns True if no empty cell is left, False otherwise 
    """
    for row in board:
        if '' in row:
            return False
    return True

def getCurrentScore() -> int:
    """ 
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """
    sum = 0
    for row in board:
        for cell in row:
            if isinstance(cell, int): #checks if cell is an int
                sum += cell
    return sum

def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """
    global board #issue with local variable

    if move == 'A': #left
        new_board = []
        for row in board:
            new_row = cellSlideLeft(row)
            new_board.append(new_row)
        board = new_board 

    elif move == 'D': #right
        new_board = []
        for row in board:
            new_row = cellSlideLeft(row[::-1]) #reverse order
            new_board.append(new_row[::-1])
        board = new_board 

    elif move == 'W': #up
        # Apply transpose to use columns as rows
        transposed_board = []
        for column in zip(*board): #pairs rows as columns
            transposed_board.append(list(column))
        
        new_board = []
        for row in transposed_board:
            new_row = cellSlideLeft(row)
            new_board.append(new_row)
        
        board = []
        for column in zip(*new_board): #transpose board back
            board.append(list(column))

    elif move == 'S': #down
        # Apply transpose to use columns as rows
        transposed_board = []
        for column in zip(*board): #pairs rows as columns
            transposed_board.append(list(column))
        
        new_board = []
        for row in transposed_board:
            new_row = cellSlideLeft(row[::-1]) #reverse order
            new_board.append(new_row[::-1])
        
        board = []
        for column in zip(*new_board): #transpose board back
            board.append(list(column))

#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line

def cellSlideLeft(row: list[int]) -> list[int]:
    """
        slides numbers left and merges adjacent same numbers per row
        returns updated row
    """
    compact = []
    for cell in row:
        if cell != '':
            compact.append(cell) #remove empty cells and compact row
    skip_merge = False #to not merge same cells twice

    for i in range(len(compact) - 1):
        if skip_merge:
            skip_merge = False
        if compact[i] == compact[i+1]:
            compact[i] *= 2 #double value of merged cell
            compact[i+1] = ''
            skip_merge = True
    
    new_compact = []
    for cell in compact:
        if cell != '':
            new_compact.append(cell)
    compact = new_compact #slide after merge
    return compact + [''] * (len(row) - len(compact)) #rest of cells get empty

if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break
        updateTheBoardBasedOnTheUserMove(userInput)
        addANewTwoToBoard()
        displayGame()

        if isFull(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break