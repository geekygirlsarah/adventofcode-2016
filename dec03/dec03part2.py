# Advent of Code
# Dec 3, Part 2
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
possibleTriangles = 0

with open(inputFile) as f:
    while True:
        lines = []
        allNums = []
        lines.append(f.readline(-1))
        if not lines[0]:
            # End of file
            break
        lines.append(f.readline(-1))
        lines.append(f.readline(-1))

        # Parse out ints
        for i in range(0, 3):
            numsList = lines[i].split(" ")
            nums = []
            for num in numsList:
                if num.rstrip().isdigit():
                    nums.append(int(num))
            allNums.append(nums)

        # Find triangles
        for i in range(0, 3):
            if (allNums[0][i] + allNums[1][i] > allNums[2][i] and
                allNums[1][i] + allNums[2][i] > allNums[0][i] and
                allNums[0][i] + allNums[2][i] > allNums[1][i]):
                    possibleTriangles += 1

print ("Number of possible triangles: " + str(possibleTriangles))
