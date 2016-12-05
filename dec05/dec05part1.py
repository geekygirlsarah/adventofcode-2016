# Advent of Code
# Dec 5, Part 1
# @geekygirlsarah

import hashlib

# Test value below
# input = "abc"
input = "uqwqemis"
password = ""
iter = 0

# Use this as quick way to debug "abc"
#iter = 3231920
while len(password) < 8:
    # status counter
    iter += 1
    if iter % 100000 == 0:
        print ("#" + str(iter))
    # Calculate hash
    m = hashlib.md5()
    m.update(input + str(iter))

    # Start with five 0s?
    d = m.hexdigest()[0:5]
    if d == "00000":
        # Add in single char to pass
        print("Found:  #" + str(iter) + " - " + m.hexdigest())
        char = m.hexdigest()[5]
        password += char

print ("Password: " + password)

