f = open("day3.in", "r+")
everything = f.read()
potentialparse = everything.split('mul')
def mul(x,y):
  return x*y
answer = 0

print(potentialparse)

for item in potentialparse:
  if len(item) > 1:
    stack = []
    start = False
    for char in item:
      if char == '(':
        start = True
      if char.isdigit():
        stack.append(char)
      if char == ',' and start:
        print(f'stack is {stack}')
        num1 = ''
        while len(stack) > 0:
          num1 += stack.pop()
      if char == ')' and len(stack) > 0 and start:
        print(f'stack is {stack}')
        num2 = ''
        while len(stack) > 0:
          num2 += stack.pop()
        print(f'num1 is {num1[::-1]}, num2 is {num2[::-1]}')
        answer += mul(int(num1), int(num2))
        start = False
        break
  

    

print(answer)