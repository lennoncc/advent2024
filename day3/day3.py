import re
f = open("day3.in", "r+")
everything = f.read()
isolatedmul = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',everything)
answer = 0
for pair in isolatedmul:
  answer += (int(pair[0])*int(pair[1]))

print(answer)
f.close()

# Part 2
f = open("day3.in", "r+")
everything = f.read()
search = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", everything)
# print(search)
dobool = True
answer = 0
for pair in search:
  if dobool and pair[0].isdigit() and pair[1].isdigit():
    answer += (int(pair[0])*int(pair[1]))
  elif pair[3] == "don't()":
    dobool = False
  elif pair[2] == "do()":
    dobool = True

print(answer)




