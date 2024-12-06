f = open("day4.in", "r+")
everything = f.readlines()
everything = [item.strip() for item in everything]
def check(x,y,grid):
  # x is row, y is col
  # diagonal
  letters = ['X','M','A','S']
  matches = 0
  found = True
  for i in range(4):
    # Forwards XMAS
    try:
      if grid[x+i][y] != letters[i]:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, forwards')
  found = True
  for i in range(4):
    # Backwards SAMX
    try:
      if grid[x-i][y] != letters[i]:
        found = False
        break
      elif x-i < 0:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, backwards')
  found = True
  for i in range(4):
    # Downwards XMAS
    try:
      if grid[x][y+i] != letters[i]:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, downwards')
  found = True
  for i in range(4):
    # Upwards XMAS
    try:
      if grid[x][y-i] != letters[i]:
        found = False
        break
      elif y-i < 0:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, upwards')
  found = True
  for i in range(4):
    # Down Right XMAS
    try:
      if grid[x+i][y+i] != letters[i]:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, dr')
  found = True
  for i in range(4):
    # Down Left SAMX
    try:
      if grid[x-i][y+i] != letters[i]:
        found = False
        break
      elif x-i < 0:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, dl')
    for i in range(4):
      print(x-i,y+i)
  found = True
  for i in range(4):
    # Up Right XMAS
    try:
      if grid[x+i][y-i] != letters[i]:
        found = False
        break
      elif y-i < 0:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, ur')
  found = True
  for i in range(4):
    # Up Left XMAS
    try:
      if grid[x-i][y-i] != letters[i]:
        found = False
        break
      elif x-i < 0 or y-i < 0:
        found = False
        break
    except:
      found = False
      break
  if found:
    matches += 1
    print(f'Found match at {x},{y}, ul')
    for i in range(4):
      print(x-i,y-i)
  
  return matches
  
  
count = 0
for i in range(len(everything)):
  for j in range(len(everything[0])):
    # if i < len(everything)-4 and j < len(everything[0])-4:
    count += check(i,j,everything)
print(count)