import re
f = open("day3.in", "r+")
everything = f.read()
isolatedmul = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',everything)
answer = 0
for pair in isolatedmul:
  answer += (int(pair[0])*int(pair[1]))

print(answer)