# student name:   Seiya Nozawa-Temchenko
# student number: 34838482

# A command-line 2048 game

import random
import copy

board: list[list] = []  # a 2-D list to keep the current status of the game board
history: list[list[list[int]]] = [] #stack of board history
MAX_HISTORY = 3

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
        
        EXTRA FEATURE: U (to undo) MAX_HISTORY times only if game is not over
    """
    print("Enter one of WASD (move Up, Left, Down, Right), U (to undo), or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'U', 'Q'): # a valid move direction or 'U' or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", "U", or "Q"') # otherwise inform the user about valid input
    return move


def addANew2Or4ToBoard() -> None:
    """ 
        adds a new 2 with probability 2/3 or a 4 with probability 1/3 at an available randomly-selected cell of the board
        new values will not neighbor same value for an immediate merge
    """
    empty_cells = []
    for row in range(4):
        for column in range(4):
            if board[row][column] == '':
                empty_cells.append((row, column)) #check empty cells

    if not empty_cells:
        return
    
    if random.random() < 2/3: #select probability 0-1
        value = 2
    else:
        value = 4
    
    harder_cells = []
    for (row, column) in empty_cells:
        same_neighbor = False
        for (offset_row, offset_column) in [(-1,0),(1,0),(0,-1),(0,1)]: #up, down, left, right
            neighbor_row, neighbor_column = row + offset_row, column + offset_column
            if 0 <= neighbor_row < 4 and 0 <= neighbor_column < 4:
                if board[neighbor_row][neighbor_column] == value:
                    same_neighbor = True
                    break #don't need to check other neighbors
        if not same_neighbor:
            harder_cells.append((row, column))

    if harder_cells:
        add_cell = random.choice(harder_cells)
    else:
        add_cell = random.choice(empty_cells) #empty cell if none
    
    board[add_cell[0]][add_cell[1]] = value

def isFullAndNoValidMove() -> bool:
    """ 
        returns True if no empty cell is left and no follow-up valid move will cause a slide/merge, False otherwise 
    """
    for row in board:
        if '' in row:
            return False
    
    for row in range(len(board)): #check if horizontal neighbors are same
        for column in range(len(board[0])-1):
            if board[row][column] == board[row][column + 1]:
                return False
            
    for row in range(len(board)): #check if vertical neighbors are same
        for column in range(len(board[0])-1):
            if board[row][column] == board[row + 1][column]:
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

def movePossible(move: str) -> bool:
    """
    checks if move changes board
    returns True if the move is possible, changing board, False otherwise.
    """
    board_copy = copy.deepcopy(board) #copy board fully
    
    if move == 'A': #left
        new_board = []
        for row in board:
            new_row = cellSlideLeft(row)
            new_board.append(new_row)

    elif move == 'D': #right
        new_board = []
        for row in board:
            new_row = cellSlideLeft(row[::-1]) #reverse order
            new_board.append(new_row[::-1])

    elif move == 'W': #up
        # Apply transpose to use columns as rows
        transposed_board = []
        for column in zip(*board): #pairs rows as columns
            transposed_board.append(list(column))
        
        new_transposed = []
        for row in transposed_board:
            new_row = cellSlideLeft(row)
            new_transposed.append(new_row)
        
        new_board = []
        for column in zip(*new_transposed): #transpose board back
            new_board.append(list(column))

    elif move == 'S': #down
        # Apply transpose to use columns as rows
        transposed_board = []
        for column in zip(*board): #pairs rows as columns
            transposed_board.append(list(column))
        
        new_transposed = []
        for row in transposed_board:
            new_row = cellSlideLeft(row[::-1]) #reverse order
            new_transposed.append(new_row[::-1])
        
        new_board = []
        for column in zip(*new_transposed): #transpose board back
            new_board.append(list(column))
    
    else:
        return False
    
    return new_board != board_copy 

if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break
        
        if userInput == 'U':
            if history:
                board = history.pop #revert to previous board
                print("Undo previous move.")
                displayGame()
            else:
                print("Invalid input.")
            continue #re-prompt user
        else:
            copy_board = copy.deepcopy(board)
            history.append(copy_board)

            if len(history) > MAX_HISTORY: #maximum 3 undos
                history.pop(0) #removes oldest history

            full_board = True #isFull-ish loop to enable input-based game over
            for row in board:
                for cell in row:
                    if cell == '':
                        full_board = False
                        break
                if not full_board:
                    break
            
            if full_board:
                if movePossible(userInput):
                    updateTheBoardBasedOnTheUserMove(userInput)
                    addANew2Or4ToBoard()
                    displayGame()
                else: #invalid move and end game
                    print("Invalid move")
                    print("Game is Over. Check out your score.")
                    print("Thanks for playing!")
                    break
            else: #board is not full yet, as normal
                updateTheBoardBasedOnTheUserMove(userInput)
                addANew2Or4ToBoard()
                displayGame()

            if isFullAndNoValidMove(): #game is over once all moves are not possible
                print("Game is Over. Check out your score.")
                print("Thanks for playing!")
                break