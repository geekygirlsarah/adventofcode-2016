# Advent of Code
# Dec 7, Part 1
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
alphabets = []
finalWord = ""

# Store the number of alphabet trackers for the length of the first line
with open(inputFile) as f:
    line = f.readline(-1)
    l = len(line) - 1
    for char in line:
