# Advent of Code
# Dec 1, Part 2
# @geekygirlsarah

import struct

inputFile = "input.txt"

# Tracking vars
x = 0
y = 0
facing = "N"
places = []
placesX = []
placesY = []
firstTwiceVisitedPlace = ""
firstTwiceVisitedPlaceDist = 0

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
        # Hey, ya gotta start somewhere...
        place = "x = " + str(x) + ", y = " + str(y)
        places.append(place)
        placesX.append(x)
        placesY.append(y)
        for coord in coords:
            dir = coord[0]
            num = int(coord[1:])
            xchange = 0
            ychange = 0
            if dir == "L":
                # print("Left " + str(num) + " blocks")
                if facing == "N":
                    facing = "W"
                    xchange = -1
                elif facing == "E":
                    facing = "N"
                    ychange = 1
                elif facing == "S":
                    facing = "E"
                    xchange = 1
                elif facing == "W":
                    facing = "S"
                    ychange = -1
            elif dir == "R":
                # print("Right " + str(num) + " blocks")
                if facing == "N":
                    facing = "E"
                    xchange = 1
                elif facing == "E":
                    facing = "S"
                    ychange = -1
                elif facing == "S":
                    facing = "W"
                    xchange = -1
                elif facing == "W":
                    facing = "N"
                    ychange = 1
            for i in range(0, num):
                x = x + xchange
                y = y + ychange
                place = "x = " + str(x) + ", y = " + str(y)
                places.append(place)
                placesX.append(x)
                placesY.append(y)
                # print("Place: " + place)
            # print ("Places:", places)
            # Check for duplicate places
            if firstTwiceVisitedPlace == "":
                for p1 in range(0, len(places)):
                    for p2 in range (p1 + 1, len(places)):
                        if places[p1] == places[p2]:
                            # print ("Found second place: " + places[p1])
                            # print ("Found second place X: " + str(placesX[p1]))
                            # print ("Found second place Y: " + str(placesY[p1]))
                            firstTwiceVisitedPlace = places[p1]
                            firstTwiceVisitedPlaceDist = abs(placesX[p1]) + abs(placesY[p1])
                # Add it either way
                # places.append(place)
            else:
                break

# print ("X = " + str(x))
# print ("Y = " + str(y))
# print ("Distance = " + str(abs(x) + abs(y)))
print ("First twice visited place = " + firstTwiceVisitedPlace)
print ("First twice visited place distance = " + str(firstTwiceVisitedPlaceDist))


