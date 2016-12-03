# Advent of Code
# Dec 3, Part 1
# @geekygirlsarah

inputFile = "input.txt"

# Tracking vars
possibleTriangles = 0

with open(inputFile) as f:
    while True:
        line = f.readline(-1)
        if not line:
            break

        # Grab 3 numbers
        numsList = line.split(" ")
        nums = []
        for num in numsList:
            print("Num: " + str(num))
            if num.rstrip().isdigit():
                nums.append(int(num))

        # Could also do Pythagorean Theorem, but went for the actual way puzzle said to solve
        # Also squaring large 3 digit numbers could take a while
        if (nums[0] + nums[1] > nums[2] and
            nums[1] + nums[2] > nums[0] and
            nums[0] + nums[2] > nums[1]):
            possibleTriangles += 1


print ("Number of possible triangles: " + str(possibleTriangles))
