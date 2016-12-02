# Advent of Code
# Dec 2, Part 1
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
finalCode = ""
lastNumber = 5      # start here
tempNumber = 0

with open(inputFile) as f:
    while True:
        line = f.readline(-1)
        if not line:
            # print "End of file"
            break
        # print ("Line: ", line)

        print ("First number=" + str(lastNumber))
        for dir in line:
            print("dir=" + dir)
            if dir == "U":
                tempNumber = lastNumber - 3
            elif dir == "D":
                tempNumber = lastNumber + 3
            elif dir == "L":
                tempNumber = lastNumber - 1
            elif dir == "R":
                tempNumber = lastNumber + 1
            elif dir == "\n":
                break

            # Boundary checks to undo out of bounds
            if dir == "U" and tempNumber < 1:
                tempNumber = lastNumber
            elif dir == "D" and tempNumber > 9:
                tempNumber = lastNumber
            elif dir == "L" and (tempNumber == 0 or tempNumber == 3 or tempNumber == 6):
                tempNumber = lastNumber
            elif dir == "R" and (tempNumber == 10 or tempNumber == 7 or tempNumber == 4):
                tempNumber = lastNumber

            print ("New number: " + str(tempNumber))
            lastNumber = tempNumber

        # last number validated, so add to code
        finalCode = finalCode + str(tempNumber)

print("Final code: " + finalCode)
