# student name:   Seiya Nozawa-Temchenko
# student number: 34838482
import multiprocessing as mp

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    numbers = set() #set to track numbers used in column

    for i in range(9):
        value = puzzle[i][column]
        
        if not isinstance(value, int) or value < 1 or value > 9:
            print(f"Column {column} not valid") #check if value is between 1-9
            return
        
        if value in numbers:
            print(f"Column {column} not valid") #check for duplicates
            return
        
        numbers.add(value)
    
    print(f"Column {column} valid")

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    numbers = set() #set to track numbers used in row

    for i in range(9):
        value = puzzle[row][i]
        
        if not isinstance(value, int) or value < 1 or value > 9:
            print(f"Row {row} not valid") #check if value is between 1-9
            return
        
        if value in numbers:
            print(f"Row {row} not valid") #check for duplicates
            return
        
        numbers.add(value)
    
    print(f"Row {row} valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    numbers = set() #set to track numbers used in subgrid 
    start_row = (subgrid // 3) * 3
    start_col = (subgrid % 3) * 3 

    for r in range (3):
        for c in range(3):
            value = puzzle[start_row + r][start_col + c]

            if not isinstance(value, int) or value < 1 or value > 9:
                print(f"Subgrid {subgrid} not valid")
                return
            
            if value in numbers:
                print(f"Subgrid {subgrid} not valid")
                return
            
            numbers.add(value)
    
    print(f"Subgrid {subgrid} valid")


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test2   #modify here for other testcases
    SIZE = 9

    process = []

    for col in range(SIZE):  #checking all columns
        p = mp.Process(target=checkColumn, args=(testcase, col))
        process.append(p)

    for row in range(SIZE):  #checking all rows
        p = mp.Process(target=checkRow, args=(testcase, row))
        process.append(p)

    for subgrid in range(SIZE):   #checking all subgrids
        p = mp.Process(target=checkSubgrid, args=(testcase, subgrid))
        process.append(p)

    for p in process:
        p.start() #starts all processes without waiting for each one to finish (parallel)
    
    for p in process:
        p.join() #blocks execution until process finishes

    #Why does p in process: p.start(); p.join() not work?
    #Makes program run one process at a time instead of at once (not multiprocessing)