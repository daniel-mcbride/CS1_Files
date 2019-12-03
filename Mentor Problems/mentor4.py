def xyz_there(xyzString):
    subIndex = xyzString.find("xyz")

    if subIndex > 0:
        dotIndex = subIndex - 1

        if xyzString[dotIndex] == ".":
            return True
        else:
            return False
    else:
        return False

testString = "xyz."

print(xyz_there(testString))
