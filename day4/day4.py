f = open("test.in", "r+")
everything = f.readlines()
everything = [item.strip() for item in everything]
def check(x,y,grid):
  # diagonal
  letters = ['X','M','A','S']
  lettersinversed = ['S','A','M','X']
  # Diagonally
  # X
  #  M
  #   A
  #    S
  for i in range(4):
    if grid[x+i][y+i] != letters[i]:
      return False
  # Backwards Diagonally
  # S
  #  A
  #   M
  #    X
  for i in range(3,-1,-1):
    if grid[x+i][y+i] != lettersinversed[i]:
      return False
  # Diagonally reversed
  #    S
  #   A
  #  M
  # X
  for i in range(4):
    if grid[x+i][y-i] != letters[i]:
      return False
  # Backwards Diagonally reversed
  #    X
  #   M
  #  A
  # S
  for i in range(3,-1,-1):
    if grid[x+i][y-i] != lettersinversed[i]:
      return False
  # Forwards
  # XMAS
  for i in range(4):
    if grid[x+i][y] != letters[i]:
      break
  # Backwards
  # SAMX
  for i in range(3,-1,-1):
    if grid[x+i][y] != lettersinversed[i]:
      break
  # Downwards
  # X
  # M
  # A
  # S
  for i in range(4):
    if grid[x][y+i] != letters[i]:
      break
  # Upwards
  # S
  # M
  # A
  # X
  for i in range(3,-1,-1):
    if grid[x][y+i] != lettersinversed[i]:
      break
  
  

for i in range(len(everything)):
  for j in range(len(everything[0])):
    if i < len(everything)-4 and j < len(everything[0])-4:
      print(check(i,j,everything))