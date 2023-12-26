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

def solve(board, col, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])
        return
    
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1, solutions)
            board[i][col] = 0

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
    solutions = []
    solve(board, 0, solutions)
    
    if len(solutions) == 0:
        print("No solution exists")
    else:
        i=1
        for solution in solutions:
            print(i)
            printsol(solution, n)
            print('\n')
            i+=1

final_solve()