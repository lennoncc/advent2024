f = open("day2.in", "r+")

# Put into list to make easier to parse through
lines = f.readlines()
# Remove newlines
lines = [line.strip() for line in lines]
reports = [report.split() for report in lines]
reports = [[int(num) for num in report] for report in reports]

def checkSafety(report):
  isDecreasing = False
  if report[0] - report[1] > 0:
    isDecreasing = True
  elif report[0] == report[1]:
    return False
  for i in range(0,len(report)-1):
    if not (abs(report[i]-report[i+1]) >= 1 and abs(report[i]-report[i+1]) <= 3 and isDecreasing == (report[i]-report[i+1] > 0)):
      return False
  return True

numTrue = 0
for report in reports:
  if checkSafety(report):
    numTrue += 1

print(numTrue)

# Part 2
numTrue = 0
for report in reports:
  # Check report if it's safe, if it is just keep count
  if checkSafety(report):
    print(f'Safe: {report}')
    numTrue += 1
  # If not, apply dampener
  else:
    for i in range(len(report)):
      if checkSafety(report[:i]+report[i+1:]):
        numTrue += 1
        print(f'Safe with {report[i]} removed, {report}')
        break
    print(f'Unsafe: {report}')
print(numTrue)