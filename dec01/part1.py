# Advent of Code
# Dec 1, Part 1
# @geekygirlsarah

import struct

inputFile = "input.txt"

# Tracking vars
x = 0
y = 0
facing = "N"

with open(inputFile) as f:
    while True:
        contents = f.readline(-1)
        if not contents:
            # print "End of file"
            break
        # print ("Contents: ", contents)
        coords = contents.split(", ")
        # print ("Split contents: ")
        # print (coords)
        for coord in coords:
            dir = coord[0]
            num = int(coord[1:])
            if dir == "L":
                print("Left " + str(num) + " blocks")
                if facing == "N":
                    facing = "W"
                    x = x - num
                elif facing == "E":
                    facing = "N"
                    y = y + num
                elif facing == "S":
                    facing = "E"
                    x = x + num
                elif facing == "W":
                    facing = "S"
                    y = y - num
            elif dir == "R":
                print("Right " + str(num) + " blocks")
                if facing == "N":
                    facing = "E"
                    x = x + num
                elif facing == "E":
                    facing = "S"
                    y = y - num
                elif facing == "S":
                    facing = "W"
                    x = x - num
                elif facing == "W":
                    facing = "N"
                    y = y + num
            print("Now facing " + facing)
            print("  x = " + str(x) + ", y = " + str(y))
print ("X = " + str(x))
print ("Y = " + str(y))
print ("Distance = " + str(abs(x) + abs(y)))
