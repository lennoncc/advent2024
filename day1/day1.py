# Start of day 1!
# Read in file input
f = open("day1.in", "r+")
# Put into list to make easier to parse through
lines = f.readlines()
# Remove newlines
lines = [line.strip() for line in lines]
# Separate into separate lists
list1 = [int(line.split()[0]) for line in lines]
list2 = [int(line.split()[1]) for line in lines]
list1.sort()
list2.sort()
sumdistance = 0
for i in range(len(list1)):
  sumdistance += abs(list1[i] - list2[i])
print(sumdistance)