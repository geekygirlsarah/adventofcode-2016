# Advent of Code
# Dec 3, Part 2
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
possibleTriangles = 0
allNums = []

with open(inputFile) as f:
    while True:
        line = f.readline(-1)
        if not line:
            # print "End of file"
            break
        # print ("Line: ", line)

        numsList = line.split(" ")
        nums = []
        for num in numsList:
            # print("Num: " + str(num))
            if num.rstrip().isdigit():
                nums.append(int(num))
        allNums.append(nums)

# print(nums)
while len(allNums) > 2:
    for i in range(0, 3):
        # print (str(i))
        print ("Triangle " + str(i) + ": " + str(allNums[0][i]) + " " + str(allNums[1][i]) + " " + str(allNums[2][i]))
        if (allNums[0][i] + allNums[1][i] > allNums[2][i] and allNums[1][i] + allNums[2][i] > allNums[0][i] and allNums[0][i] + allNums[2][i] > allNums[1][i]):
            possibleTriangles = possibleTriangles + 1
    del allNums[0:3]

print ("Number of possible triangles: " + str(possibleTriangles))
