# Advent of Code
# Dec 4, Part 2
# @geekygirlsarah

import re

inputFile = "input.txt"

# Tracking vars
letterUsage = []
sumSectorIds = 0
commonLetters = ['a'] * 5
commonLettersCount = [0] * 5

with open(inputFile) as f:
    while True:
        line = f.readline(-1)
        if not line:
            break

        # Grab 3 numbers
        letterUsage = [0] * 26
        for char in line:
            ascii = ord(char) - 97
            if char == '-':
                continue
            if ascii < 0:
                break
            if char == '[':  # just in case
                break
            letterUsage[ascii] += 1

        parts = re.split(r"[\[\]-]", line)

        sizeParts = len(parts)
        checksum = sizeParts - 2
        sectorId = sizeParts - 3

        maxCount = 0
        maxLetter = 'a'
        for i in range(0, 26):  # through letterusage
            if letterUsage[i] > maxCount:
                maxLetter = chr(i+97)
                maxCount = letterUsage[i]
        commonLetters[0] = maxLetter
        commonLettersCount[0] = maxCount

        maxCount = 0
        maxLetter = 'a'
        for i in range(0, 26):  # through letterusage
            if letterUsage[i] > maxCount:
                if commonLetters[0] == chr(i+97):
                    continue
                maxLetter = chr(i+97)
                maxCount = letterUsage[i]
        commonLetters[1] = maxLetter
        commonLettersCount[1] = maxCount


        maxCount = 0
        maxLetter = 'a'
        for i in range(0, 26):  # through letterusage
            if letterUsage[i] > maxCount:
                if commonLetters[0] == chr(i+97) or commonLetters[1] == chr(i+97):
                    continue
                maxLetter = chr(i+97)
                maxCount = letterUsage[i]
        commonLetters[2] = maxLetter
        commonLettersCount[2] = maxCount

        maxCount = 0
        maxLetter = 'a'
        for i in range(0, 26):  # through letterusage
            if letterUsage[i] > maxCount:
                if commonLetters[0] == chr(i+97) or commonLetters[1] == chr(i+97) or commonLetters[2] == chr(i+97):
                    continue
                maxLetter = chr(i+97)
                maxCount = letterUsage[i]
        commonLetters[3] = maxLetter
        commonLettersCount[3] = maxCount

        maxCount = 0
        maxLetter = 'a'
        for i in range(0, 26):  # through letterusage
            if letterUsage[i] > maxCount:
                if commonLetters[0] == chr(i+97) or commonLetters[1] == chr(i+97) or commonLetters[2] == chr(i+97) or commonLetters[3] == chr(i+97):
                    continue
                maxLetter = chr(i+97)
                maxCount = letterUsage[i]
        commonLetters[4] = maxLetter
        commonLettersCount[4] = maxCount



        # for i in range(ord('a'), ord('z')):
        #     for j in range(0, 5):
        #         if letterUsage[i] > commonLettersCount[j]:
        #             for k in range(j+1, 5):
        #                 commonLetters[k+1] = commonLetters[k]
        #                 commonLettersCount[k+1] = commonLettersCount[k]
        #                 commonLetters[j] = i
        #                 commonLettersCount[j] = letterUsage[i]


        if ("".join(commonLetters) == parts[int(checksum)]):
            print("VALID!")
            # print ("Top 5 letters: ")
            # print (commonLetters)
            print ("Code: " + parts[int(checksum)])
            sumSectorIds += int(parts[int(sectorId)])

            # Decrypt
            sectorMod = int(parts[int(sectorId)]) % 26 # why shift hundreds when you can shift a little?
            decryptedLine = ""
            for c in line:
                if c == '-':
                    decryptedLine += " "
                    continue
                if c == "[" or c.isdigit():
                    break
                ascii = (ord(c) - 97) + sectorMod
                if ascii > 25:
                    ascii %= 26
                ascii += 97
                c = chr(ascii)
                decryptedLine += c
            print ("Decrypted line: " + decryptedLine)
            if decryptedLine == "northpole object storage ":
                print ("SECTION ID: " + parts[int(sectorId)])

print ("Sum of sector IDs: " + str(sumSectorIds))

