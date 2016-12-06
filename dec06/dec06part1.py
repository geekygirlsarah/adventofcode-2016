# Advent of Code
# Dec 6, Part 1
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
alphabets = []
finalWord = ""

# Store the number of alphabet trackers for the length of the first line
with open(inputFile) as f:
    line = f.readline(-1)
    l = len(line) - 1
    for i in range (0, l):
        alphabet = []
        for j in range (0, 26):
            alphabet.append(0)
        alphabets.append(alphabet)

# Look at each row, add it's value to each alphabet tracker
with open(inputFile) as f:
    while True:
        line = f.readline(-1)
        if not line:
            break

        for i in range (0, len(line)):
            char = line[i]
            if char == "\n":
                break
            pos = ord(char) - 97
            alphabets[i][pos] += 1

# Find the max letter from each alphabet tracker, print out final word
print("Word: ")
for alphabet in alphabets:
    maxIndex = alphabet.index(max(alphabet))
    finalWord += chr(maxIndex + 97)
print(finalWord)
