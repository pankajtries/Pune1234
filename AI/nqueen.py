def printSolution(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()

def isSafe(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    return not (slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row])

def solveNQueensUtil(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    global count
    if col >= N:
        count += 1
        printSolution(board)
        return True
    for row in range(N):
        if isSafe(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
            board[row][col] = 1
            rowLookup[row] = slashCodeLookup[slashCode[row][col]] = backslashCodeLookup[backslashCode[row][col]] = True
            if solveNQueensUtil(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
                pass
            board[row][col] = 0
            rowLookup[row] = slashCodeLookup[slashCode[row][col]] = backslashCodeLookup[backslashCode[row][col]] = False
    return False

def solveNQueens(N):
    global count
    count = 0
    board = [[0 for _ in range(N)] for _ in range(N)]
    slashCode = [[row + col for col in range(N)] for row in range(N)]
    backslashCode = [[row - col + N - 1 for col in range(N)] for row in range(N)]
    rowLookup = [False] * N
    slashCodeLookup = [False] * (2 * N - 1)
    backslashCodeLookup = [False] * (2 * N - 1)
    solveNQueensUtil(board, 0, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)
    if count == 0:
        print("Solution does not exist")
        return False
    else:
        print("Total solutions:", count)
        return True

N=int(input("Enter the number of queens: "))
solveNQueens(N)
