n = 8
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1 or board[i][col] ==1:
            return False
    
    i = row
    j = col
    while i >= 0 and j >= 0: #upper main diagonal
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while i < n and j >= 0: # lower secondary diagonal
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
        
    i = row
    j = col
    
    while i < n and j < n: #main diagonal
        if board[i][j] == 1:
            return False
        i += 1
        j += 1
    
    i = row
    j = col
    while i >=0 and j >= 0: #secondary diagonal
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
 
    return True
def solve(board, col):
    if col >= n:
        return True
    
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1) == True:
                return True
    
        board[i][col] = 0
    return False

def printsol(s,n):
    for i in range(n):
        for j in range(n):
            if s[i][j] == 1:
                print('q', end=' ')
            else:
                print('.', end=' ')
        print('\n')

def final_solve():
    board = [[0 for i in range(n)] for j in range(n)]
    if solve(board, 0) == False:
        print("No solution exists")
    else:
        printsol(board,n)
        
final_solve()