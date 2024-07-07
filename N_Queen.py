def check_column(board, row, column):
  """
  Checks if a queen can be placed in a specific column without attacking any existing queen in the same column.
  """
  for i in range(row, -1, -1):
    if board[i][column] == 1:
      return False
  return True

def check_diagonal(board, row, column):
  """
  Checks if a queen can be placed in a specific position without attacking any existing queen diagonally (both upper left and upper right diagonals).
  """
  # Check upper left diagonal
  for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
    if board[i][j] == 1:
      return False
  
  # Check upper right diagonal
  for i, j in zip(range(row, -1, -1), range(column, len(board))):
    if board[i][j] == 1:
      return False
  
  return True

def nqn(board, row):
  """
  Solves the N-queens problem using backtracking.
  """
  if row == n:
    return True
  
  for i in range(n):
    if check_column(board, row, i) and check_diagonal(board, row, i):
      board[row][i] = 1
      if nqn(board, row + 1):
        return True
      board[row][i] = 0
  return False

n = int(input("Enter the value of n: "))
board = [[0 for i in range(n)] for j in range(n)]

if nqn(board, 0):
  print("Solution:")
  for row in board:
    print(row)
else:
  print("No solution exists.")


            
            
            


             


        
           
        

