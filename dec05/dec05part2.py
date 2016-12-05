# Advent of Code
# Dec 5, Part 2
# @geekygirlsarah

import hashlib

# Test value below
#input = "abc"
input = "uqwqemis"
password = "xxxxxxxx"
iter = 0

# Use this as quick way to debug "abc"
#iter = 3231920
while "x" in password:
    # status counter
    if iter % 100000 == 0:
        print ("#" + str(iter))
    # Calculate hash
    m = hashlib.md5()
    m.update(input + str(iter))

    # Start with five 0s?
    d = m.hexdigest()[0:5]
    if d == "00000":
        print("Found:  #" + str(iter) + " - " + m.hexdigest())
        # get position and character. replace only if it hasn't been calculated yet and position os 0-7
        pos = int(m.hexdigest()[5], 16)
        char = m.hexdigest()[6]
        if pos < 8:
            if password[pos] == "x":
                # Swap out single position
                password = password[0:pos] + char + password[pos+1:]
                print("New password: " + password)

    iter += 1

print ("Password: " + password)
