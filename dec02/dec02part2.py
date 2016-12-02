# Advent of Code
# Dec 2, Part 1
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
finalCode = ""
lastNumber = 5      # start here
tempNumber = lastNumber

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
                if lastNumber == 3:
                    tempNumber = lastNumber - 2
                if lastNumber > 5 and lastNumber < 9:
                    tempNumber = lastNumber - 4
                if lastNumber >= 10 and lastNumber <= 12:
                    tempNumber = lastNumber - 4
                if lastNumber == 13:
                    tempNumber = lastNumber - 2
            elif dir == "D":
                if lastNumber == 1:
                    tempNumber = lastNumber + 2
                if lastNumber >= 2 and lastNumber <= 4:
                    tempNumber = lastNumber + 4
                if lastNumber >= 6 and lastNumber <= 8:
                    tempNumber = lastNumber + 4
                if lastNumber == 11:
                    tempNumber = lastNumber + 2
            elif dir == "L":
                if lastNumber == 6:
                    tempNumber = lastNumber - 1
                if lastNumber == 3 or lastNumber == 7 or lastNumber == 11:
                    tempNumber = lastNumber - 1
                if lastNumber == 4 or lastNumber == 8 or lastNumber == 12:
                    tempNumber = lastNumber - 1
                if lastNumber == 9:
                    tempNumber = lastNumber - 1
            elif dir == "R":
                if lastNumber == 5:
                    tempNumber = lastNumber + 1
                if lastNumber == 2 or lastNumber == 6 or lastNumber == 10:
                    tempNumber = lastNumber + 1
                if lastNumber == 3 or lastNumber == 7 or lastNumber == 11:
                    tempNumber = lastNumber + 1
                if lastNumber == 8:
                    tempNumber = lastNumber + 1
            elif dir == "\n":
                break

            lastNumber = tempNumber
            print ("New number: " + str(lastNumber))


        # last number validated, so add to code
        lastChar = str(lastNumber)
        if lastNumber == 10:
            lastChar = "A"
        elif lastNumber == 11:
            lastChar = "B"
        elif lastNumber == 12:
            lastChar = "C"
        elif lastNumber == 13:
            lastChar = "D"
        finalCode = finalCode + lastChar

print("Final code: " + finalCode)
